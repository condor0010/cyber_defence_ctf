podman build -t vsftpd-test .
podman run -it --rm -v $(pwd):/data vsftpd-test
