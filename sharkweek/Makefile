default:
	echo "dose nothing"
solve:
	tshark -r dun_dun.pcapng -T fields -e tcp.payload | tr -d '\n' | xxd -r -p > out.png
clean:
	rm out.png
