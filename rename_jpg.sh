x=0
for i in $(ls | grep jpg | grep -v rename_jpg.sh); do
  echo "mv $i $x.jpg" | sh -
  x=$((x+1))
done
