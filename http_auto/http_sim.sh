#!/bin/sh
nohup sh -c 'python3 -m http.server 8000 & sleep 10s; kill $!' > /dev/null 2>&1 &
nohup sh -c 'tcpdump -i lo -w ./capture.pcap -W 1000 & sleep 10s; kill $!' > /dev/null 2>&1 &
sleep 1; curl http://0.0.0.0:8000/flag.jpg > /dev/null 2>&1
