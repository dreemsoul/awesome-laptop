#!/usr/bin/python

import imaplib

M=imaplib.IMAP4_SSL("MAIL ADDRESS", 993)
M.login("USERNAME","PASSWORD")

status, counts = M.status("Inbox","(MESSAGES UNSEEN)")

unread = counts[0].split()[4][:-1]

print(int(unread))

M.logout()
