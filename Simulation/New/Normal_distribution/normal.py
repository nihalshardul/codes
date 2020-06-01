from data_iat import iat
from plot import d,b,s,nt,yz,k		# d=min b=max  s=interval_size and nt=intervals and yz=observed_frequency k = interval
import math
import numpy as np

mean = sum(iat)/len(iat)	#mean
n=len(iat)			# n 
sigma_sq = 0		#sigma square
pi=3.14		#value of pi


sigma=np.std(iat)	#sigma
sigma_sq=(sigma)**2	#sigma_square
print ("sg_sq :",sigma_sq)
print ("sg :",sigma)
#fst = 1/(sigma*(np.sqrt(2*pi)))	# 1/sqrt(2_pi_sigma.sq)

def chi_square(ob_fq,E):
        chi=[]
        for i in range(0,len(ob_fq)):
                m=(ob_fq[i]-E[i])**2/E[i]
                chi.append(m)
        return sum(chi)

def tpdl(fn,sml_h):
	h=sml_h/2
	w = len(fn)
	mid_sum=0
	for i in range(1,len(fn)-1):
		mid_sum += fn[i]
	mid_sum = 2*mid_sum
	
	re = h*(fn[0]+fn[w-1]+mid_sum)
	return (re)


def ex(x):
	e=(1/(math.sqrt(2*pi*sigma_sq)))*(math.exp(-(1/2)*((x-mean)/sigma)**2))
	#print (e)
	return (e)

def i_p(h,l):
	sml_h = (h-l)/100
	lw=l
	ar_in = []		#array of interval from ai to ai+1
	while(lw<h):
		ar_in.append(lw)
		lw+=sml_h
	#print (len(ar_in))		
	fn=[]			#value for f(x) for each f(xi)
	for xi in ar_in:
		f=0
		f= ex(xi)
		fn.append(f)
		
	#print ("Arr :",ar_in)
	#print ("For p:",fn)	
	Ep=tpdl(fn,sml_h)	#trapazaoidal funtion
	Ei = Ep*n
	return (Ei)

a=d	#minimum of data
b=b	#maximum of data
h=s	#interval size
print ("mean  :",mean)
print ("min :",a,"max :",b,"interval size :",h)

it = nt

print ("Intervals : ",it)	#intervals
#print (len(nt))

ob_fq=yz

print ("Observed Frequency : ",ob_fq)
#print (len(ob_fq))

E=[]
for i in range(0,len(it)-1):
#	i_p(it[i+1],it[i])	#interval_probability
	it_pb = i_p(it[i+1],it[i])	#interval_probability
	E.append(it_pb)
#	break
#E.append(0)
print ("Expected Freq :",E)
#print (len(E))
#print ("IAT :",iat)

chi_value=chi_square(ob_fq,E)
print ("chi_value :",chi_value)
