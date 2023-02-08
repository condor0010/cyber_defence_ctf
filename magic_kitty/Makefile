default:
	cp orig.jpg chall.jpg
	dd if=/dev/zero bs=2 count=1 conv=notrunc of=chall.jpg
clean:
	rm chall.jpg
solve:
	echo -ne \\xff\\xd8 | dd of=chall.jpg bs=1 count=2 conv=notrunc

