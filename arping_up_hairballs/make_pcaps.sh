python main.py hint.txt hint.txt.pcap &
python main.py img/0.jpg pcap/0.pcap &
python main.py img/1.jpg pcap/1.pcap &
python main.py img/2.jpg pcap/2.pcap &
python main.py img/3.jpg pcap/3.pcap &
wait
mergecap -w out.mergecap -w out.pcap pcap/0.pcap pcap/1.pcap pcap/2.pcap pcap/3.pcap

