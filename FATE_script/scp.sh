tar -xf ${2}.tar ${2}/

if [ "$1" =  "root" ]
then
	ip="192.168.151.52"
	user="gzqq"
else
	user="fate"
	if [ "$1" = "client0" ]
	then
		ip="192.168.86.134"
	elif [ "$1" = "client1" ]
	then
		ip="192.168.86.132"
	elif [ "$1" = "client2" ]
	then
		ip="192.168.86.133"
	elif [ "$1" = "client3" ]
	then
		ip="192.168.86.136"
	else
		echo "invalid destination"

	fi
fi

scp ${2}.tar ${user}@${ip}:/home/${user}/Desktop

rm -rf ${2}.tar
