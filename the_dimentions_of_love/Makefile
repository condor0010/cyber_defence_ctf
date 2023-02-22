default:
	cp orig.png chall.png
	dd if=/dev/zero bs=1 seek=16 count=8 conv=notrunc of=chall.png
clean:
	rm chall.png
solve:
	echo -ne '\x00\x00\x05\xA0\x00\x00\x05\xA0' | dd of=chall.png bs=1 seek=16 conv=notrunc


