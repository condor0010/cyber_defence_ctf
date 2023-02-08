default:
	cp orig.jpg chall.jpg
	exiftool -Comment="FLAG{wow_i_am_so_happy_i_think_ill_byte_your_leg}" chall.jpg
	rm chall.jpg_original
clean:
	rm chall.*
solve:
	strings chall.jpg | grep FLAG
