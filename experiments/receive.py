#!/usr/bin/env python

from carbon_telegram.network import Receiver
import sys

TOKEN=sys.argv[1]

recv = Receiver(TOKEN)
