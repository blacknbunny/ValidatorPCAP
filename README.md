# ValidatorPCAP
This tool allows you to find ip addresses in PCAP file by making comparison between two list of ip addresses to bypass windows firewall {inbound/outbound} rules by exporting ip addresses to txt file from windows firewall GUI.

![image](https://user-images.githubusercontent.com/33333043/112559965-2737e800-8de3-11eb-8231-6128f0718217.png)
![image](https://user-images.githubusercontent.com/33333043/112560059-6403df00-8de3-11eb-8e82-a8f4ffe6b45a.png)

## Usage

First execute bash file to extract ip addresses that captured from any computer which involved in network activity of any application that we want to compare with other list named as "iplist.txt" the picture shows us how to export blocked/allowed ip addresses from windows firewall gui.

Bash file will write ip addresses in PCAP file to the .txt file named as "incomingiplist.txt".
```
chmod +x tcpdumpextractipfrompcap.sh
./tcpdumpextractipfrompcap.sh capturednetworkpackets.pcap
```

![image](https://user-images.githubusercontent.com/33333043/112561615-a2e76400-8de6-11eb-8e56-db25dfd957b2.png)


After you export "iplist.txt" from windows firewall and execute the bash file to create "incomingiplist.txt" includes ip addresses that you want to find in "iplist.txt", you have to execute "compare_blockedip_address.py" to compare two list to find same ip addresses.

```
C:\Users\*-*\Desktop\unblockingmicrosoftipaddress>python compare_blockedip_address.py
Found An IP Address : 13.107.18.11
Found An IP Address : 13.107.21.200
Found An IP Address : 13.107.42.12
Found An IP Address : 13.107.6.254
Found An IP Address : 52.114.132.91
Found An IP Address : 52.158.24.209
Found An IP Address : 40.125.122.151
Found An IP Address : 40.70.229.150
Found An IP Address : 52.155.217.156
Found An IP Address : 52.155.223.194
```

## Description
The reason i made this tool is most of us doesn't even knows what Inbound/Outbound rules is defined in *Windows Defender Firewall* (Can it cause a damage ?, Are all these rules the same as the rules we want?, etc..).

Basically what im tryna say is by learning what rules came from us and what rules doesn't came from us we can Accept/Reject it.

With this tool you can track the network activity of the application that Inbound/Outbound rules are defined by *Windows Defender Firewall* as Accepted/Rejected.

# What else this tool can be used by ?
We can use it as a "network activity tracker" by tracking the network activity of the application that we want by disabling the Accept/Reject rule in *Windows Defender Firewall Advanced Security GUI* then comparing the ip address/adresses that defined as a rule by *Windows Firewall* with the ip adress/adresses captured in our computer via (Wireshark, tcpdump, etc..) and saved as (PCAP/PCAPNG) file. etc...

