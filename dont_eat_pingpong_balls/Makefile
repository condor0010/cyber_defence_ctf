default:
	python icmp_gen.py hint.txt
	python icmp_gen.py flag.jpg
solve:
	tshark -r flag.jpg.pcap -T fields -e data | tr -d '\n' | xxd -r -p  > out.jpg
clean:
	rm *.pcap
	rm out.jpg
