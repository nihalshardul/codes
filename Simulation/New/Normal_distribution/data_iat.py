import re
import sys
import math

file_name = sys.argv[1]		#pass file name  to this file i.e. python read_csv_file.py data.csv
fs = open(file_name,'r')
k=[]
for i in fs.readlines():	#read line by line
	k.append(int(i))
print ("Original data => ",k)				#stores file in list
print (len(k))

iat=k		#iat => inter_arival_time

"""for i in range(0,len(k)):
	if i==0:
		d=k[i].split(":")	#d[0]  -- int (minute)
		m=d[1].split(".")	#m[0] -- int(second) && m[1] - float(milisecond)
		p=int(d[0])*60+int(m[0])+float("0."+m[1])	#we convert time in float number

	else:
		d=k[i].split(":")	#d[0]  -- int (minute)
		m=d[1].split(".")	#m[0] -- int(second) && m[1] - float(milisecond)
		x=int(d[0])*60+int(m[0])+float("0."+m[1])	#we convert time in float number
		iat.append(round(x-p,2))	#round up float value upto two decimal i.e. 12.9468888888 => 12.94
		p=x

print ("Inter arival time =>",iat)
print (len(iat))		# no. of observations(n)
"""
