
sudo rm -rf /home/nihal/spc/config/  /home/nihal/spc/data/
cd /home/nihal/spc/patil_sir/postgresql-9.3.0/
sudo make clean
./configure --without-readline --without-zlib --prefix=/home/nihal/spc/config
sudo make -j 12
sudo make install
mkdir /home/nihal/spc/data
sudo chown postgres /home/nihal/spc/data/
