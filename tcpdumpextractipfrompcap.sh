#!/bin/bash
tcpdump -r $1 'ip' -n | grep -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' -o | sort -u > incomingiplist.txt
