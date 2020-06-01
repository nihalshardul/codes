def bwc():
	n=int(input())
	a = [int(x) for x in raw_input().split()]
	b = [int(x) for x in raw_input().split()]
	cnt=0
	j=0
	a.sort()
	b.sort()	
	for i in range(0,len(a)):
		if a[i]>b[j]:
			cnt+=1
			j+=1
	return cnt

def main():
	n=int(input())
	while(n!=0):
		print bwc()
		n-=1

main()
