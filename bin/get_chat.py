#!/usr/bin/python3

import requests
import json
import sys
import argparse
import datetime
import re

HOST = "owasp.slack.com"
HISTORY_RESOURCE_PATH = "/api/conversations.history"
REPLIES_RESOURCE_PATH = "/api/conversations.replies"
USERS_LIST_RESOURCE_PATH = "/api/users.list"
USER_INFO_RESOURCE_PATH = "/api/users.info"
CHANNEL_ID = "CBKGH8A5P"

users = {}


def run(fromtime, totime, token, maxout=None):
    data = {}
    if fromtime is not None:
        oldest = datetime.datetime.timestamp(
            datetime.datetime.strptime(fromtime, "%Y-%m-%d %H:%M:%S")
        )
        data["oldest"] = oldest

    if totime is not None:
        latest = datetime.datetime.timestamp(
            datetime.datetime.strptime(totime, "%Y-%m-%d %H:%M:%S")
        )
        data["latest"] = latest

    outcnt = 0
    while True:
        resp = send_request(HISTORY_RESOURCE_PATH, token, extra_data=data).json()
        if outcnt == 0 and len(resp["messages"]) == 0:
            print(f"No messages for {fromtime} - {totime}. Wrong date?")
            breakpoint()
            sys.exit()

        outcnt += 1
        with open(f"out_{outcnt:03d}.json", "w") as fp:
            midx = 0
            for m in resp["messages"]:
                if "user" in m and m["user"] not in users:
                    users[m["user"]] = get_user_info(m["user"], token)
                if "users" in m:
                    for u in m["users"]:
                        if u not in users:
                            users[u] = get_user_info(u, token)
                grp = re.findall("<@[A-Z0-9]+>", m["text"])
                for p in grp:
                    u = p.replace("<@", "").replace(">", "")
                    if u not in users:
                        users[u] = get_user_info(u, token)
                if "thread_ts" in m:
                    replies = get_replies(m["thread_ts"], token)
                    resp["messages"][midx]["replies"] = replies
                    for rp in replies["messages"]:
                        grp = re.findall("<@[A-Z0-9]+>", rp["text"])
                        for p in grp:
                            u = p.replace("<@", "").replace(">", "")
                            if u not in users:
                                users[u] = get_user_info(u, token)
                midx += 1
            print(
                f"Writing data to out_{outcnt:03d}.json with {len(resp['messages'])} items..."
            )
            fp.write(json.dumps(resp, indent=4, sort_keys=True))

        if "response_metadata" in resp and "next_cursor" in resp["response_metadata"]:
            data["cursor"] = resp["response_metadata"]["next_cursor"]
        else:
            print("No more next_cursor, exiting")
            break

        if maxout is not None and maxout == outcnt:
            print(f"Reached max number of outputs ({maxout}). Skipping rest")
            break

    with open("users.json", "w") as fp:
        fp.write(json.dumps(users, indent=4, sort_keys=True))


def send_request(resource_path, token, extra_data=None):
    data = {"token": token, "channel": CHANNEL_ID}
    if extra_data is not None:
        for key, value in extra_data.items():
            data[key] = value
    return requests.post(f"https://{HOST}{resource_path}", data=data)


def get_user_info(user, token):
    return send_request(
        USER_INFO_RESOURCE_PATH, token, extra_data={"user": user}
    ).json()


def get_replies(thread_timestamp, token):
    return send_request(
        REPLIES_RESOURCE_PATH, token, extra_data={"ts": thread_timestamp}
    ).json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool to fetch conversations from Slack channel"
    )
    parser.add_argument(
        "-f",
        "--from",
        dest="fromtime",
        metavar='"%s"' % (datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")),
        type=str,
        help="From date and time",
        required=False,
    )
    parser.add_argument(
        "-t",
        "--to",
        dest="totime",
        metavar='"%s"' % (datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")),
        type=str,
        help="From date and time",
        required=False,
    )
    parser.add_argument(
        "-m",
        "--max",
        dest="maxout",
        metavar="N",
        type=int,
        help="Max number of pieces of output",
        required=False,
    )
    parser.add_argument(
        "-T",
        "--token",
        dest="token",
        metavar="STR",
        type=str,
        help="Slack API token",
        required=False,
    )
    args = parser.parse_args()

    if args.fromtime is None and args.totime is None and args.maxout is None:
        print("You must pass at least -f (from) and -t (to) OR -m (max) argument")
        sys.exit()

    if args.token is None:
        print("You must pass the Slack API tokenn via -T / --token")
        sys.exit()

    run(args.fromtime, args.totime, args.token, maxout=args.maxout)
