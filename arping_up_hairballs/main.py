from scapy.all import ARP, Ether, sendp, wrpcap
import sys

target_ip = f"10.8.0.10{sys.argv[1][4]}"

print(target_ip)
with open(sys.argv[1], "rb") as f:
    file_contents = f.read()

file_bytes = list(file_contents)

pkts = []
for byte in file_bytes:
    hex_str = hex(byte)[2:].zfill(2)
    
    dest_mac = f"00:00:00:00:00:{hex_str}"
    
    ether_pkt = Ether(dst=dest_mac)
    arp_pkt = ARP(op=2, pdst=target_ip, hwdst=dest_mac, psrc=target_ip, hwsrc=ether_pkt.src)
    
    pkts.append(ether_pkt/arp_pkt)

wrpcap(sys.argv[2], pkts)
