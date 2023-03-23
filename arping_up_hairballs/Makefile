default:
	sf
solve:
	tshark -r out.pcap -Y "arp.src.proto_ipv4==10.8.0.103" -T fields -e eth.dst | awk -F ':' '{printf "%s", $6}' | xxd -r -p > flag.jpg
clean:
	rm flag.jpg
