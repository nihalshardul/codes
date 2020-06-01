import matplotlib.pyplot as plt
from data_iat import iat
import math

a=min(iat)
b=max(iat)
print (a,b)

mp=iat[1:]+[0]

k=10

s=(b-a)/k

print (s)

#xxx=[a]
xxx=[]
#a=s
while (a<=b+s):
	xxx.append(round(a,3))
	a+=s
xxx.append(round(a,3))

print (xxx)
print (len(xxx))
yz=[]

for i in range(0,len(xxx)-1):
	cnt=0
	for j in iat:
		if (xxx[i] <= j < xxx[i+1]):
			cnt+=1
	yz.append(cnt)
yz.append(0)
print (yz)
print(len(yz))

plt.scatter(iat,mp)
plt.show()
#plt.hist(xxx,yz,normed=1,facecolor='blue', alpha=0.5)
plt.xticks(range(len(yz)), xxx)
plt.bar(xxx,yz,align='center')
plt.xlabel('Range')
plt.ylabel('Frequency')
#plt.gcf().autofmt_xdate()
plt.show()

