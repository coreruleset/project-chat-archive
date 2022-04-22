#!/bin/bash

if [ -z "$TOKEN" ]; then
	echo "ENV variable \$TOKEN is not set. This is fatal. Aborting."
	exit 1
fi

cat chat-dates.txt | while read MYDATE; do
	echo -n "Handling chat of $MYDATE ... "
	if [ ! -f chat-archive-$MYDATE.md -a ! -z chat-archive-$MYDATE.md ]; then
		./bin/get-chat.py  -f "$MYDATE 20:30:00" -t "$MYDATE 23:55:00" -T $TOKEN
		./bin/chat2md.py -d . -o chat-archive-$MYDATE.md
		rm out_*.json
		echo "done"
	else
		echo "already existing"
	fi
done
rm users.json
