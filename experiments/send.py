#!/usr/bin/env python

from carbon_telegram.network import Sender
import sys

TOKEN=sys.argv[1]
CHAT=sys.argv[2]

lines = []
while True:
	send = Sender(TOKEN, CHAT)

	line = sys.stdin.readline().rstrip()
	if line == '.':
		send.send("\n".join(lines))
		lines = []
	else:
		lines.append(line)

	