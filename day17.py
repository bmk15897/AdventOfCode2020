
# DAY 17

import numpy as np
import collections

def getNeighbours(cube):
	dim = len(cube.shape)       # number of dimensions
	offsets = [-1, 1]     # offsets, 0 first so the original entry is first 
	columns = []
	for shift in itertools.product(offsets, repeat=dim):   # equivalent to dim nested loops over offsets
		columns.append(np.roll(cube, shift, np.arange(dim)).ravel())
	neighbors = np.stack(columns, axis=-1)
	return neighbors
def cubes():
	l,r = 0,7
	s = 8
	active = set()
	for i in range(s):
		t = list(input())
		for j in range(s):
			if int(t[j]) == 1:
				active.add((i,j,0,0))
	for _ in range(6):
		new_active = active.copy()
		for i in range(l-1,r+2):
			for j in range(l-1,r+2):
				for k in range(l-1,r+2):
					for a in range(l-1,r+2):
						cnt = 0
						for x in range(i-1,i+2):
							for y in range(j-1,j+2):
								for z in range(k-1,k+2):
									for w in range(a-1,a+2):
										if (x,y,z,w)!=(i,j,k,a) and (x,y,z,w) in active:
											cnt+=1
						if (i,j,k,a) in active:
							if cnt not in [2,3]:
								new_active.remove((i,j,k,a))
						else:
							if cnt == 3:
								new_active.add((i,j,k,a))
		l-=1
		r+=1
		active = new_active.copy()
	print(len(new_active))
							
	
cubes()


""" Input

##..#.#.
#####.##
#######.
#..#..#.
#.#...##
..#....#
....#..#
..##.#..

"""