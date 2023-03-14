default:
	python arp_gen.py hint.txt.pcap hint.txt
	python arp_gen.py distrib.pcap 0.jpg  1.jpg  2.jpg  3.jpg  4.jpg
	#mkdir distrib
	#mv *.pcap distrib
	#tar -czvf distrib.tar.gz distrib
	#rm -rf distrib
solve:
	tshark -r  distrib.pcap | awk -F ":" '/10\.8\.0\.6/ {printf "%s", substr($9,1,2)}'  |  xxd -r -p > out.jpg
clean:
	rm *.tar.gz *.pcap out 2>/dev/null
