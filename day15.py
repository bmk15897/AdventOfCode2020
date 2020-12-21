
# Day 15


def elvesMemGame():
	ind = {1:[2],14:[1],3:[3],7:[4],9:[5], 0:[0]}
	c = 6
	ok = [0,14,1,3,7,9]
	#ok = [1,2,3]
	#ind = {1:[0],2:[1],3:[2],0:[]}
	while c!=30000000:
		if (len(ind[ok[-1]]))==1:
			ok.append(0)
			ind[0].append(c)
		else:
			t = ok[-1]
			te = ind[t][-1]-ind[t][-2]
			ok.append(te)
			if te not in ind:
				ind[te] = [c]
			else:
				i = ind[te]
				if len(i)==2:
					i.pop(0)
				i.append(c)
		c+=1
	print(c)
	print(ind)
	print(ok)
	
elvesMemGame()


""" Input

0,14,1,3,7,9

"""