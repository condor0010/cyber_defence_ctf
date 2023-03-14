from scapy.all import *

# Set up the target IP address and port number
target_ip = "192.168.0.2"
ftp_port = 21

# Set up the FTP commands and file data
ftp_user = "USER anonymous\r\n"
ftp_pass = "PASS testuser@testdomain.com\r\n"
ftp_retr = "RETR test_file.txt\r\n"
file_data = "This is the content of the test file."

# Set up the TCP connection
syn = IP(dst=target_ip)/TCP(dport=ftp_port, flags="S")
syn_ack = sr1(syn)
ack = IP(dst=target_ip)/TCP(dport=ftp_port, flags="A", seq=syn_ack.ack, ack=syn_ack.seq + 1)

# Send the FTP commands
payload = ftp_user + ftp_pass + ftp_retr
ftp_request = IP(dst=target_ip)/TCP(dport=ftp_port, sport=ack[TCP].dport, seq=ack[TCP].ack, ack=ack[TCP].seq + len(payload), flags="PA")/Raw(load=payload)
ftp_response = sr1(ftp_request)

# Send the file data
file_request = IP(dst=target_ip)/TCP(dport=ftp_port, sport=ack[TCP].dport, seq=ftp_response[TCP].ack, ack=ftp_response[TCP].seq + len(ftp_response[Raw]), flags="PA")/Raw(load=file_data)
file_response = sr1(file_request)

# Close the TCP connection
fin = IP(dst=target_ip)/TCP(dport=ftp_port, sport=ack[TCP].dport, seq=file_response[TCP].ack, ack=file_response[TCP].seq + len(file_response[Raw]), flags="FA")
fin_ack = sr1(fin)

# Save the packets to a PCAP file
wrpcap("ftp_download.pcap", [syn, syn_ack, ack, ftp_request, ftp_response, file_request, file_response, fin, fin_ack])

