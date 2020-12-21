
# Day 13

def bus():
	s = int(input())
	b = input().split(',')
	a = []
	ok = []
	for i in b:
		if i!='x':
			ok.append(int(i))
	k = 0
	print(ok)
	flag=True
	while flag==True:
		for i in ok:
			if (s+k)%i==0:
				print(k*i)
				flag=False
				break
		k+=1
	
#bus()

def bus2():
	b = input().split(',')
	t = 17
	k = 0
	ok = []
	for i in b:
		if i!='x':
			ok.append(int(i))
	p = 0
	flag = True
	while flag == True:
		f = True
		for n,i in enumerate(b):
			print(t)
			if i!='x' and f!=False:
				if (t+n)%int(i)==0:
					print('oh yes')
				else:
					f = False
		if f==True:
			print(t)
			flag=False
		t+=17
		
#bus2()


from sympy.ntheory.modular import crt

with open('C:\\Users\\Kulkarni\\Desktop\\o.txt') as f:
    timestamp = int(next(f))
    busses = [(int(bus), -i)
              for i, bus in enumerate(next(f).split(',')) if bus != 'x']
			  
print(crt(*zip(*busses))[0])


""" Input

1000186
17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,907,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,29,x,653,x,x,x,x,x,x,x,x,x,41,x,x,13

"""
