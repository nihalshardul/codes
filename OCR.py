def pow_grl():
	n=int(input())
	qu = [int(x) for x in raw_input().split()]
	ing = [int(x) for x in raw_input().split()]
	d=0
	cnt=0

	while(True):
		for i in range(0,len(qu)):
			ing[i]-=qu[i]
		for i in ing:
			if i < 0:
				d=i
		if d<0:
			break
		cnt+=1
	return cnt

def main():
	print pow_grl()



main()