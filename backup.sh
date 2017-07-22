if test "${1}" == '' 
then
	echo "Enter with output filename"
else
	tar -cf ${1} *
	gzip ${1}
fi