import matplotlib.pyplot as plt
from data_iat import iat
import math

a=min(iat)
b=max(iat)		#max of inter_arival is stored in b
#print (a,b)
d=a			#minimun of inter_arival is stored in a
mp=iat[1:]+[0]

k=int(input("Intervals : "))

s=(b-a)/k

#print (s)

#nt=[a]
nt=[]
#a=s
while (a<=b):
	nt.append(round(a,3))
	a+=s		#a is getting updated
#nt.append(round(a,3))		#Intervals

#print (nt)
#print (len(nt))
yz=[]			# Observed Frequency

for i in range(0,len(nt)-1):
	cnt=0
	for j in iat:
		if (nt[i] <= j < nt[i+1]):
			cnt+=1
	yz.append(cnt)
#print (yz)
#print(len(yz))

plt.scatter(iat,mp)
plt.show()
#plt.hist(nt,yz,normed=1,facecolor='blue', alpha=0.5)
plt.xticks(range(len(yz)), nt)
plt.bar(nt,yz+[0],align='center')
plt.plot(nt,yz+[0],color='red')
plt.xlabel('Range')
plt.ylabel('Frequency')
#plt.gcf().autofmt_xdate()
plt.show()

