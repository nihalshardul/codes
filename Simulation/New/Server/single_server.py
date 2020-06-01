import random
import math
#it=[2.6,0.13,1.2,1.89,4.32,1.94,1.12,1.42,2.3,1.3]
#ser=[3.1,2.3,1.1,0.2,2.8,1.9,3.4,3.5,1.1,1.9]

#it=[2.6,0.13,1.2,1.89,2.32,1.92,5.42,2.34,2.54,1.3]
#ser=[3.1,2.3,3.8,1.2,1.0,0.51,2.51,2.0,1.0,3.2]


it=[]           #inter_arival_time		--weibull 
ser=[]          #service_time			--uniform 

alpha=3
beta=2
a=2
b=3

for i in range(0,100):
        u=random.random()
        x=alpha*math.pow((-(math.log(1-u))),1/beta)
        it.append(round(x,3))
        x=a+((b-a)*u)
        ser.append(round(x,3))




c=[]
clk=0
w_t=[]
s_t=[]
s_e=[]
server=0		#server is idel
q=0			#queue
D=float('inf')		#Departure
i=1
j=0
p=0
A=it[0]			#Arival
clk=0			#current clk
c.append(clk)
que=[]

while(len(w_t)<len(it)):		#while(i!=len(it) and j!=len(ser)):		#while(len(w_t) != len(it)):
	if A<D:
		clk=A
		if server==0:
			server=1
			c.append(clk)
			ser_start=clk			
			service=ser[j]			#service_time	=> st
			j+=1
			ser_end=ser_start+service
			D=ser_end
			s_t.append(ser_start)			#service_start	=> s_t
			s_e.append(ser_end)		#service_end	=> s_e
			wt=s_t[p]-c[p]
			w_t.append(wt)
			p+=1
		else:
			q+=1
			que.append(q)
		#print (i)
		if (i<len(it)):
			A=A+it[i]
			i+=1
		else:
			A=float('inf')
		
	else:
		clk=D
		#print(D)
		if q==0:
			server=0
			D=float('inf')
		else:
			q-=1
			c.append(clk)
			ser_start=clk			
			service=ser[j]			#service_time	=> st
			j+=1
			ser_end=ser_start+service
			D=ser_end
			s_t.append(ser_start)			#service_start	=> s_t
			s_e.append(ser_end)		#service_end	=> s_e
			wt=s_t[p]-c[p]
			w_t.append(wt)
			p+=1
			que.append(q)
#print (s_t)
#print (s_e)
#print (A)

print("Sr.no. \t inter_arival_time \t clock \t\t service \t service_start \t service_end \t wating_time \t queue")

for i in range(0,len(it)):
        print(i+1,"\t",it[i],"\t\t\t",round(c[i],3),"\t\t",round(ser[i],3),"\t\t",round(s_t[i],3),"\t\t",round(s_e[i],3),"\t\t",round(w_t[i],3),'\t\t',que[i])


