
# DAY 23

def cyclic_equiv(u, v):
    n, i, j = len(u), 0, 0
    if n != len(v):
        return False
    while i < n and j < n:
        k = 1
        while k <= n and u[(i + k) % n] == v[(j + k) % n]:
            k += 1
        if k > n:
            return True
        if u[(i + k) % n] > v[(j + k) % n]:
            i += k
        else:
            j += k
    return False
		
def cups():
	arr = [int(i) for i in "389125467"]
	arr.extend([i for i in range(10,1000000+1)])
	cntr = 0
	
	currCup = 0
	lst = arr
	
	#rounds = []
	
	while cntr!=10000000:
		print(cntr)
		#print("Curr List",lst)
		print("currCup",currCup)
		currCupLabel = lst[currCup]
		print("currCupLabel", currCupLabel)
		#print(rounds)
		#flag = 0
		#for i in rounds:
		#	if currCupLabel == i[1] and cyclic_equiv(lst,i[0]) == 1:
		#		flag = i[2][-1]
		
		#if flag!=0:
		#	cntr+=(cntr-flag)
		#	continue
		#else:
		#	rounds.append([lst,currCupLabel,cntr])
		
		a = lst[(currCup+1)%1000000]
		
		b = lst[(currCup+2)%1000000]

		c = lst[(currCup+3)%1000000]
		toBePicked = [a,b,c]
		lst.pop(lst.index(a))
		lst.pop(lst.index(b))
		lst.pop(lst.index(c))
		arr = lst.copy()
		
		
		print("to be picked",toBePicked)
		
		destCupLabel = currCupLabel-1
		if destCupLabel == 0:
			destCupLabel = 999999
		while (destCupLabel in toBePicked):
			destCupLabel = destCupLabel - 1
			if destCupLabel == 0:
				destCupLabel = 999999
		destCup = lst.index(destCupLabel)
		print("DestCupLabel", destCupLabel)
		lst = arr[:destCup+1]
		lst.extend(toBePicked)
		lst.extend(arr[destCup+1:])
		currCup = lst.index(currCupLabel)
		if currCup+1>999999:
			currCup = 0
		else:
			currCup +=1
		cntr+=1
	print(lst)
#cups()

class Cup:
	def __init__(self, data):
		self.data = data
		self.next = None

def cups2():
	arr = [int(i) for i in "872495136"]
	arr.extend([i for i in range(10,1000000+1)])
	cups = [Cup(k) for k in arr]
	for i in range(1000000-1):
		cups[i].next = cups[i+1]
	cups[1000000-1].next = cups[0]
	curRefs = {cup.data: cup for cup in cups}
	curCup = cups[0].data
	for _ in range(10000000):
		p = curRefs[curCup]
		a = curRefs[curCup].next
		b = curRefs[curCup].next.next
		c = curRefs[curCup].next.next.next
		curRefs[curCup].next = c.next
		destCup = curCup
		while True:
			destCup -= 1
			if destCup < 1:
				destCup = 1000000
			if destCup not in [a.data, b.data, c.data]:
				break
		c.next = curRefs[destCup].next
		curRefs[destCup].next = a
		curRefs[destCup].next.next = b
		curRefs[destCup].next.next.next = c
		curCup = curRefs[curCup].next.data

	print(curRefs[1].next.data)
	print(curRefs[1].next.next.data ) 
	
cups2()