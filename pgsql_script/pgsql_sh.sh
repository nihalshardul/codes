confirm_config=/home/nihal/spc/config
psql_path=/home/nihal/spc/patil_sir/postgresql-9.3.0/
conf=configure
new_data_file=/home/nihal/spc/data
psql_user=postgres

if [ -d $confirm_config ]
 then
        echo "Removing Config and Data files"
        sudo rm -rf /home/nihal/spc/config/  /home/nihal/spc/data/
else
        echo "Config and Data file not present"
fi

echo "Moving in POSTGRESQL path for Installation"
cd $psql_path           # In/home/nihal/spc/patil_sir/postgresql-9.3.0/

echo "Make clean is performing for new Postgress Installation"
sudo make clean

if [ -f $conf ]
 then
	echo "Making Configuration ... "
	./configure --without-readline --without-zlib --prefix=/home/nihal/spc/config
else
	echo " No Configuration file is present ... "
fi

echo "Making setup Faster with more jobs ..."
sudo make -j 12

echo "Making Instalation for postgresql"
sudo make install


if [ -d $new_data_file ]
 then
	echo "Data file is already present"
else
	mkdir $new_data_file
fi

sudo chown $psql_user $new_data_file		#/home/nihal/spc/data/
