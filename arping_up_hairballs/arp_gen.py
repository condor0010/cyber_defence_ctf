from scapy.all import ARP, Ether, sendp, wrpcap
import sys

output_pcap_file = sys.argv[1]
input_files = sys.argv[2:]

target_ip_prefix = "10.8.0."
ip_address_count = len(input_files)

pkts = []
for i, input_file in enumerate(input_files):
    with open(input_file, "rb") as f:
        file_contents = f.read()

    file_bytes = list(file_contents)

    # Calculate the IP address for this file
    target_ip = target_ip_prefix + str(i+3)

    for byte in file_bytes:
        hex_str = hex(byte)[2:].zfill(2)

        dest_mac = f"00:00:00:00:00:{hex_str}"

        ether_pkt = Ether(dst=dest_mac)
        arp_pkt = ARP(op=2, pdst=target_ip, hwdst=dest_mac, psrc=target_ip, hwsrc=ether_pkt.src)

        pkts.append(ether_pkt/arp_pkt)

wrpcap(output_pcap_file, pkts)

