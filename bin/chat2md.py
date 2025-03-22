#!/usr/bin/python3
import glob
import sys
import argparse
import datetime
import os
import json
import re
import html

users = {}


def ord(n):
    return str(n) + (
        "th" if 4 <= (n % 100) <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    )


def dtStylish(dt, f):
    return dt.strftime(f).replace("{th}", ord(dt.day))


def transform(t, users):
    # set the #NNNN format as link
    grp = re.findall(r"#\d{3,}", t)
    for p in grp:
        t = t.replace(
            p, "[%s](https://github.com/coreruleset/coreruleset/issues/%s)" % (p, p)
        )

    # t = re.sub("^#", "\#", text)

    # Replace the <@USER_ID> by @Username
    # format it as _italic_
    grp = re.findall("<@[A-Z0-9]+>", t)
    for p in grp:
        p = p.replace("<@", "").replace(">", "")
        t = t.replace("<@" + p + ">", "_@%s_" % (users[p]))

    # unescape HTML entities
    t = html.unescape(t)

    return t


def get_text(message):
    if "blocks" in message:
        return transform_blocks(message["blocks"])
    else:
        return transform(message["text"], users)


def transform_blocks(blocks):
    text = ""
    for block in blocks:
        if "elements" in block:
            text += transform_block_elements(block["elements"])
        else:
            print("Error: no item 'elements' in b")
    return text


def transform_block_elements(elements):
    text = ""
    for block_element in elements:
        text += transform_text_elements(block_element)
    return text


def transform_text_elements(block_element):
    text = ""
    if "elements" in block_element:
        for element in block_element["elements"]:
            match element["type"]:
                case "text":
                    markdown = transform_rich_text(element)
                    text += transform(markdown, users)
                case "link":
                    if "text" in element:
                        text += f"[{element["text"]}]({element["url"]})"
                    else:
                        text += f"[{element["url"]}]({element["url"]})"
                case "emoji":
                    text += f":{element["name"]}:"
                case "user":
                    text += f"_@{users[element["user_id"]]}_"
                case "rich_text_section":
                    section = transform_text_elements(element)
                    for line in section.splitlines():
                        text += f"> {line}\n"
                case _:
                    print(f"Error: Unknown text element type {element["type"]}")
    else:
        print(f"Error: block element has no text elements: {block_element}")
    return text


def transform_rich_text(element):
    text = element["text"]
    if "style" in element:
        for variant, enabled in element["style"].items():
            if not enabled:
                continue

            match variant:
                case "bold":
                    text = f"**{text}**"
                case "italic":
                    text = f"_{text}_"
                case "strike":
                    text = f"<del>{text}</del>"
                case "code":
                    text = f"`{text}`"

    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MD formatted chat creation tool")
    parser.add_argument(
        "-d",
        "--directory",
        dest="directory",
        metavar="/path/to/directory",
        help="Input directory",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        metavar="file to content",
        type=str,
        help="Output file",
        required=True,
    )
    args = parser.parse_args()

    run(args.directory, args.output)


def run(directory, output):
    files = []
    try:
        for f in glob.glob("*.json", root_dir=directory):
            if f == "users.json":
                try:
                    with open(f, "r") as fp:
                        _users = json.load(fp)
                    for u in _users:
                        users[u] = _users[u]["user"]["profile"]["display_name"]
                        if users[u] == "":
                            users[u] = _users[u]["user"]["profile"]["real_name"]
                except:
                    print(sys.exc_info()[0])
                    sys.exit(1)
            else:
                files.append(f)
    except:
        print("Can't open directory: %s" % (directory))
    files.sort(reverse=True)
    lastdate = ""
    with open(output, "w") as fpo:
        for f in files:
            with open(f, "r") as fp:
                data = json.load(fp)
            for d in reversed(data["messages"]):
                ts = datetime.datetime.fromtimestamp(
                    float(d["ts"]), tz=datetime.timezone.utc
                )
                tsdate = ts.strftime("%Y-%m-%d")
                tstime = ts.strftime("%H:%M:%S %Z")
                if lastdate != tsdate:
                    fpo.write("### %s\n\n" % dtStylish(ts, "%a, %b {th}, %Y"))
                    lastdate = tsdate
                if d.__contains__("user"):
                    if d["user"] in users:
                        fpo.write(
                            '**%s** <span style="color: grey; font-size: 90%%;">%s</span>\n\n'
                            % (users[d["user"]], tstime)
                        )
                    else:
                        print("User " + d["user"] + " not in user table.")
                        fpo.write(
                            '**%s** <span style="color: grey; font-size: 90%%;">%s</span>\n\n'
                            % ("unknown user", tstime)
                        )
                else:
                    fpo.write(
                        '**%s** <span style="color: grey; font-size: 90%%;">%s</span>\n\n'
                        % ("unknown user", tstime)
                    )
                text = get_text(d)
                fpo.write('<span style="font-size: 90%%;">%s</span>\n\n' % (text))
                if "replies" in d:
                    for r in d["replies"]["messages"][1:]:
                        ts = datetime.datetime.fromtimestamp(
                            float(r["ts"]), tz=datetime.timezone.utc
                        )
                        tsdate = ts.strftime("%Y-%m-%d")
                        tstime = ts.strftime("%H:%M:%S %Z")
                        if lastdate != tsdate:
                            fpo.write("##### %s\n\n" % dtStylish(ts, "%a, %b {th}, %Y"))
                            lastdate = tsdate
                        if r.__contains__("user"):
                            if r["user"] in users:
                                fpo.write(
                                    '↳ **%s** <span style="color: grey; font-size: 90%%;">%s</span>\n\n'
                                    % (users[r["user"]], tstime)
                                )
                            else:
                                print("User " + r["user"] + " not in user table.")
                                fpo.write(
                                    '↳ **%s** <span style="color: grey; font-size: 90%%;">%s</span>\n\n'
                                    % ("unknown user", tstime)
                                )
                        else:
                            fpo.write(
                                '↳ **%s** <span style="color: grey; font-size: 90%%;">%s</span>\n\n'
                                % ("unknown user", tstime)
                            )
                        # text = transform(r['text'], users)
                        text = get_text(r)
                        # fpo.write("&nbsp;&nbsp;&nbsp;&nbsp;%s\n\n" % (text))
                        fpo.write(
                            '<span style="font-size: 90%%;">%s</span>\n\n' % (text)
                        )
