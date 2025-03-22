#!/usr/bin/env python3

import argparse
import glob
import os
import sys

import chat2md
import get_chat

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool to build chat archive from Slack"
    )
    parser.add_argument(
        "-t",
        "--token",
        dest="token",
        type=str,
        help="Slack user token",
        required=True,
    )
    args = parser.parse_args()

    directory = os.path.dirname(os.path.dirname(__file__))
    with open(os.path.join(directory, "chat-dates.txt"), "rt") as file:
        for date in file.readlines():
            date = date.strip()
            archive_md = f"chat-archive-{date}.md"
            print(f"Handling chat of {date} ... ")
            if not os.path.exists(os.path.join(directory, archive_md)):
                get_chat.run(f"{date} 20:30:00", f"{date} 23:55:00", args.token)
                chat2md.run(directory, archive_md)
                for file in glob.glob("out_*.json", root_dir=directory):
                    os.remove(file)
                print("done")
            else:
                print("already exists")

if os.path.exists("users.json"):
    os.remove("users.json")
