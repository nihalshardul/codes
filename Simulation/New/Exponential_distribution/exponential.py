from data_iat import iat
import math


def chi_square(freq,Ei):
	chi=[]
	for i in freq:
		m=(i-Ei)**2/Ei
		chi.append(m)
	return sum(chi)


ks=len(iat)/5                   #no. of maximum intervals(ks)

print ("intervals must be in 1 - ",ks)

si=int(input())         #si => selected intervals(k)

while si>ks:
        print ("value must be less than",ks)
        si=int(input())

p=1.0/si        # probability of observations falls under the class

mean = sum(iat)/len(iat)        # mean of intervals

a=[]            # intervals

for i in range(0,si):
        if i==0:
                a.append(0)
        else:
                q=-mean*math.log(1-(i*p))
                a.append(q)
print ("Range =>",a)		#range
#print (len(a))

freq=[]			#frequency for that range
for i in range(0,len(a)-1):
        cnt=0
        for j in iat:
                if (a[i] <= j < a[i+1]):
                        cnt+=1
        freq.append(cnt)

print ("frequency =>" ,freq)
#print (len(freq))

Ei = float(len(iat))/float(si)	#for finding expected value (Ei)

print ("Ei :",Ei)

chi=chi_square(freq,Ei)	#value of chi_square

print ("chi_square =>",chi)
