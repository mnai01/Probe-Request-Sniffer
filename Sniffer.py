#!/usr/bin/env python
from scapy.all import *
from datetime import datetime
import urllib2


#Holds addresses
clientprobes = []
location = "home"

def PacketHandler(pkt):
    # filter if packet is probe request
    if pkt.haslayer(Dot11ProbeReq):
       # only packes with an ssid are shown.
       # Is packet is a wildcard in wireshark it will not be shown
        if len(pkt.info) > 0:
            # shows packet mac address 
            testcase = (pkt.addr2 + '---' + pkt.info)
        else:
            pkt.info = "Unknown"
            testcase = (pkt.addr2 + '---' + pkt.info)
        if testcase not in clientprobes:
            # datetime object containing current date and time
            now = datetime.now()
            time_log = now.strftime("%m/%d/%y %H:%M:%S")
            clientprobes.append(testcase)
            print ("New Probe Found: " + pkt.addr2 + ' ' +  ' ' + pkt.info + ' ' + time_log)
            SendtoServer(pkt.addr2,pkt.info,location,time_log)

def SendtoServer(MAC,SSID,Location,Time):
    url = urllib2.quote("http://www.ianmatlak.com/add_data.php?MAC="+MAC+"&SSID="+SSID+"&Location="+Location+"&TIME="+Time+"/",':/')
    wp = urllib2.urlopen(url)
    pw = wp.read()
    print(pw)

sniff(iface="wlan0mon", prn = PacketHandler,   store=0)
print("after sniff")
