import re


incomingiplist_array = []
iplistLines_count = 0

with open('incomingiplist.txt', 'r') as inciplist:
    iplistLines = inciplist.readlines()
    iplistLines_count = len(iplistLines)
    for line in iplistLines:
        incomingiplist_array.append(line.strip())
        # print("Line{}: {}".format(count, found_ip_address[0]))
        # newfound_ip_address = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", newline.strip())
        # newfresh_ip_address = newfound_ip_address[0]
        # print(newfresh_ip_address[0])

with open('newiplist.txt', 'r') as iplist:
    iplistLines = iplist.readlines()
    for line in iplistLines:
        for i in range(0,iplistLines_count):
            if incomingiplist_array[i] == line.strip():
                print("Found An IP Address : {}".format(line.strip()))
        #print(line.strip())
        # print("Line{}: {}".format(count, found_ip_address[0]))
        # newfound_ip_address = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", newline.strip())
        # newfresh_ip_address = newfound_ip_address[0]
        # print(newfresh_ip_address[0])
