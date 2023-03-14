FROM debian:latest

RUN apt-get update && apt-get install -y vsftpd tcpdump ftp

RUN mkdir /root/ftp

# Configure vsftpd
RUN echo "listen=YES" > /etc/vsftpd.conf
RUN echo "listen_port=21" >> /etc/vsftpd.conf
RUN echo "anonymous_enable=NO" >> /etc/vsftpd.conf
RUN echo "local_enable=YES" >> /etc/vsftpd.conf
RUN echo "write_enable=YES" >> /etc/vsftpd.conf
RUN echo "local_umask=022" >> /etc/vsftpd.conf
RUN echo "dirmessage_enable=YES" >> /etc/vsftpd.conf
RUN echo "use_localtime=YES" >> /etc/vsftpd.conf
RUN echo "xferlog_enable=YES" >> /etc/vsftpd.conf
RUN echo "connect_from_port_20=YES" >> /etc/vsftpd.conf
RUN echo "chroot_local_user=YES" >> /etc/vsftpd.conf
RUN echo "secure_chroot_dir=/var/run/vsftpd/empty" >> /etc/vsftpd.conf
RUN echo "pam_service_name=vsftpd" >> /etc/vsftpd.conf
RUN echo "rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem" >> /etc/vsftpd.conf
RUN echo "rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key" >> /etc/vsftpd.conf
RUN echo "ssl_enable=NO" >> /etc/vsftpd.conf
RUN echo "chroot_local_user=YES" >> /etc/vsftpd.conf
RUN echo "local_root=/root/ftp" >> /etc/vsftpd.conf



# Create a test file to upload to the vsftpd server
RUN echo "This is a test file" > /root/ftp/test.txt

# Start the vsftpd server in the background
CMD service vsftpd start & sleep 2 && \
    # Connect to the vsftpd server and download the test file
    echo "get test.txt" | ftp -p localhost && \
    # Capture network traffic using tcpdump and save it to a file
    tcpdump -i any -w /tcpdump.pcap && \
    # Wait for tcpdump to finish writing the file
    sleep 2 && \
    # Stop the vsftpd server
    killall vsftpd

