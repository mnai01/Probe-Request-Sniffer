# Probe-Request-Sniffer

![Not news_letter](./news_letter.JPG)

Sponsored by Farmingdale State College

Tested using Kali Linux VirtualBox 32-Bit v2020.1

Python v3.8.0

**Required package:**

sudo apt-get install python-scapy

**Required equipment:**

NIC(monitor mode enabled)

**Required software**

Aircrack-ng

**Add connection credentials and place file in webserver where db is.**

**In Sniffer.py change sniff()**
```python
sniff(iface='YOUR-CARD-NAME', prn = PacketHandler, store=0)
```

**How it works**

This script uses the scapy library and a raspberry pi with a NIC in monitor mode to scan for probe requests within its local proximity. Based off its results it will POST the information count received to a backend PHP server. The count will with the time/location will be help in the database and used in the frontend to show students how busy the area is at any given time. It automatically scans throughout the day for live updating

**Table Layout**
```sql
CREATE TABLE `tbl_Probes` (
 `MAC_Address` varchar(17) NOT NULL,
 `SSID` varchar(36) NOT NULL,
 `Location` varchar(36) NOT NULL,
 `UserTime` datetime NOT NULL DEFAULT current_timestamp(),
 `ID` int(11) NOT NULL AUTO_INCREMENT,
 PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=162 DEFAULT CHARSET=utf8mb4
```
