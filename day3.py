# DAY 3

def countTrees(jumpRight):
	cnto = 0
	cntt = 0
	pos = jumpRight
	k = input()
	for _ in range(322):
		k = input()
		if k[pos%31]=='#':
			cntt+=1
		else:
			cnto+=1
		pos+=jumpRight
	return cntt

#a =countTrees(1)
#b =countTrees(3)
#c =countTrees(5)
#d =countTrees(7)

def countTreesAlter(jumpRight):
	cnto = 0
	cntt = 0
	skip = 1
	pos = jumpRight
	k = input()
	for _ in range(322):
		k = input()
		if skip%2==0:
			if k[pos%31]=='#':
				cntt+=1
			else:
				cnto+=1
			pos+=jumpRight
		skip+=1
	return cntt

#e = countTreesAlter(1)
#print(a,b,c,d,e)
#print(a*b*c*d*e)

def countTreesAlterModified(jumpRight,skipDown):
	cnto = 0
	cntt = 0
	skip = 1
	pos = jumpRight
	k = input()
	for _ in range(322):
		k = input()
		if skip%skipDown==0:
			if k[pos%31]=='#':
				cntt+=1
			else:
				cnto+=1
			pos+=jumpRight
		skip+=1
	return cntt
	
a =countTreesAlterModified(1,1)
b =countTreesAlterModified(3,1)
c =countTreesAlterModified(5,1)
d =countTreesAlterModified(7,1)
e = countTreesAlterModified(1,2)
print(a,b,c,d,e)
print(a*b*c*d*e)




""" Input

.........###......#...#.......#
.#.#...........#..#..#.........
#.......#.................#....
.........#.#.........#......###
.....#......##...##............
...##...#......#.....#.....##..
#.#..#....#...#....#......#....
........##.....#.....#.#.......
......#.....#......#...##.#....
...####...#.......##.....#.#...
.........#....#......##........
..##...........###.#...........
.....#............#............
#.#..#..##........#.....#..#...
.....................#....##..#
...........##.....###...#.#.#..
..#......#...........#.........
.##.##...#...#......##.#.......
......#..#......#.#.#..#.#.....
........#.#..#..........#...#.#
...........##...........#....#.
...........#...##.#............
.......#...........#...........
.......#......#..#...#....#..#.
..#.....#.#....#.#......#...#.#
.#..........###..#....#........
........##..#..#...#..#....#..#
#..........#...#..#.#........#.
..#.#........##.##....##.#.....
#.##....#...#.......#.#..#....#
......##...#.#.#.#.....#....#..
..........#..............#.....
....................###.#......
#.....#...#...#.#.......#....#.
.......#..#...................#
........##.##........#......#..
...#...##.#...#...........#....
..#.........#...#....##......#.
......#..............#..#..#.#.
.....##...#...#...##....#......
#.#....#...#......##.....#...##
.#...#.#..................#....
#.##.....#......#..........#...
..#..#.......#.................
..#.....#.........#........#...
.......#...##.##.#..#..##.#..#.
#.............#.........#.#....
..#..##..........#..#..##.#.#..
.#......#.......#...#.....##.#.
.....#......#...#...........###
..........#.........#.....#....
.....#..........#.......##...#.
......#..#..#..............#...
.#.####..#...##...#.#..........
..#....#.......#........#.....#
....#.##.....#..#.....#.#.#..#.
.......#..#..##.......#........
.#.....#...........#.....#.....
........#..........##..##.#....
.#.....#........#.....#..#.....
..#..........#...#......##..#..
.#............#.........#....#.
........#..###.......#.....###.
##.#...#.#..#..#..#.#.##...#...
.#....#...#..#......##.........
.............##.....##.........
.....##.#..###.#....#...#...#.#
#........#...#......#...#.##...
#....#......#.....###.##.#.....
.....#..#.#.##....#..##.....##.
....#...#...#..........##......
..........#......#...#.....##..
.....##....##.#.............#.#
#.........#.##.............#..#
.....#.........##.#...#.#.#....
..........#..#......#..#.....#.
....#....#....#....#.......###.
....#...#..##....#..##..#...##.
.###......#...........###......
#..................####.#....#.
#....#.#.....#.#....#..#.......
...#......#....##......#..#..#.
#.#...#.##.....#.#.......##..#.
.........##.................#..
#..##.#....#.#.............#...
....................####.#.#..#
.......#..#...#..#..#.....#...#
.....#.#.#........#....#...##..
......#..#....#......#..##.....
............#......##.#....#..#
...#..........#..#...........#.
..........#.............###....
....##.#.#......#.#..#....##..#
..#..........#........#......#.
..#...........####......##..#.#
...##......##...#..#.##........
.....#...#.....##.....###..##..
.#.##.....#....##....#.........
#....##..#.....#.#......#.#....
..#.......#...#....#...#.#.....
...........#.........#.........
..#..#....##..#....#....#.....#
.......#..#....##....#.........
#.........#...........##....##.
#........#.#...............##..
#...##.#...............#.......
#....#..#......#..#.###...##..#
..#.........#.#......#.....#..#
......#...........##........##.
.#.........#................#..
#...#...............#...#....#.
.#.#......##.........#.#.......
..........#....................
.#.....#..#...#.#.#.......#...#
..#..........#.................
.#.#.....#.#......#...#.....##.
.....#.#..##...##..#..###...#..
......#......#.#......#.##.....
#.#......#...#.......#....#....
..........#....#.#..#.....##...
#...........#.#....#.##....#.#.
#.#....#..#.........###....#...
..............#..##.......#....
.......................#.##.#..
##...............##....#..#.#..
.#.#..#.##...#.............#...
...#...........#............#..
..#......#........##....#.#.##.
.#.#..#........#....#....#....#
.#.....#.##....#.....#..#...#..
......#...#..........#..###....
..#.#.......#........#........#
.......##.####..........#......
.#.#..#......##..#.........#..#
..#...##.#.......#...#.##...#.#
#.#..........#..#.#.#..........
.....#......#............#.....
........###...#.......#........
.....#.##....#....#............
...#.#....##.....#.....#.......
..#.............#......#.......
.#....#...#....##..#......#....
..#.....#.#............#.......
......#........##.........#...#
.......#........#..#.#.#...##.#
#....#...#..#.......#....##....
#...##.#.#.....#.......#.......
.....#........#.#.....#...##...
..#....#..##......#.#.....#...#
....#.....#......#.....#.......
#.#....#......#...##...........
..#.......#...#...............#
........#........#.............
#.#.#......#...#..#..........#.
.##...#.........#........#..#..
#.#.#...#.#.......#.....#...#..
...#..............#..........#.
#.#...#.###.............#......
................#.....###.##.#.
.......#..........#....#..#....
......##....#..#..##...........
...#...#.....######.......#....
..##.....##.#...#.........#.#.#
.......#...#..#.#.#...........#
........###.............#...#.#
#.....#.........#.............#
..#...#.....#..................
.....#....#.....#......#.#....#
...#....#........##...#.......#
...##.#...#.....#..............
..#.##....##..#.........#......
.....#..#.#....#...#......#.#..
...........##..##...#..#..###..
#...........#.........####....#
.#...........#...........###...
........#................#.....
.....#....#............#....#.#
...#...#.......#...............
#.....##.#.......#.#...........
#.......#.#.#.#..#...#.........
....####.#...#.#......#.....##.
...##...#.....#.#......#..#....
..........#..#....#......###...
...................#....##...#.
....#......#........#...##..#..
##...#.........#.#......#......
#........#...#....#......#.....
#..#.......#...............##..
......##......#...........##.#.
......#..#....#....#.##........
..#....#..#.#.###....#.........
.#......#..#..............#....
.#..........#...#..#.#...#.....
....#......#..#......#....#....
...##.....#............####..#.
......#.#...#....#..#...#..#.#.
......##.......................
#.##........#...........####..#
.....#......#.......#.#....#...
#.......#....#.....#....#...##.
.....#..##.#...........#..#...#
...........#.##.#.#...#.#..#...
..#.......#.#....#..#..........
...#.......##..#.............#.
....#..#....#....#...#....#....
#......#.#...##..........#..#..
..#.#.......#.........#......#.
#...............#.............#
....##..#......................
.##....#............#......#...
.......#....#..##......##......
#..##.....#..#..........#......
...#.........#.......#..##.....
....#.##.....#.#...#...#.....#.
##...........#.#..#...#.#......
....#.............##...#.#..#..
...#....#......................
#..#...##.#.......#.##..#.###..
...##.#.#...##........##...#...
......##..#..#.....#..#.#..#...
#.......##...............##.#..
.##......#..#....#...##..#..#.#
##.........##..#...#.....##....
...#..........#...#..##.#......
..##.#........#...#..........##
.......................##.#....
....#...#...#..###.#.......#.##
....#....#.#..........#.##.....
..#..........##...#....#.......
.....#.....#.....#..#.........#
..##..##..#..#....#..#.......##
.............#............##...
....#.#.#.......###.........#..
...##.#..........#.#...#.#.....
.#........#..#.#.#..#..........
...##...#.....##.......#..#..#.
...#......#..#.......##.#.#....
.........#.........##........#.
.........##..................##
....##.....#................#..
....#..................##...#.#
.........#..............#......
...#......#..#..#....#..#...##.
.#.##......##...#.#......#.#...
...#.#...###....#...#.#..#....#
....#..#.......#.....#..##.#.#.
#.#.#..#.......#####.#..##..#..
#..........#.....#..#.#..#.....
.#......#...#..#.#..#..#.......
...#....##...#..........#.##.#.
#.##..#...#..................#.
......#.###..#..#..#.......#...
...#....#...#..#............###
#.........#........#.......#...
...#..#.................#....##
...#.#.............##......#...
##....#.##.............##......
#............#..#..#.....#.....
....#........#...#.....#.#...##
..#.##..#.....................#
#.#........#...#..#...#.#......
...#..#...........##.....#.....
......#.#....#..##...#.....#...
......#......#.###..##.........
....#.......#...##.##.....#....
#.....##....#........#..##.....
.#..#..#..#..#.#...#...#.......
.......##...#......#.........#.
.#..##....#.....#...........##.
.......##....#.#........#......
..#.#.#....#...................
.#...#.......#...#.#......#....
..##.##..##...........###......
#...#......#.......#...........
#....##.#.......#.........#....
.............##.#.#..#...#...#.
..##.##...........#.........##.
#.#...#..........#.#....#....##
.....#.....#..##..#............
#.........#.........#.#...##..#
...#.#.....#.........###..#....
..#.#.##.#...................#.
......####....#.......#.......#
.........#..#..#....#..##......
....#..........#...##........#.
..........#..#....#.....#....#.
.#.#.................#....#....
.......#......#.....#...##.....
....#..............#...........
###...........##.#...........#.
...####.......#...#....#.#...#.
..##.#................#........
...#..#....#.....#.....##..#...
##.#....#....##..........#.#..#
...#....#.....#................
..#...#....#..#..#.##.##..#....
....#....#.##.....#...#......#.
......#................#..#..#.
...##..#...#....#.#.....#..#...
#...#..............#.#.....#.#.
....#.........#.##...#.#....#..
..................#..##.#......
.#.....#.....#.............#..#
..........####....###..##...#..
......#........#...#......##..#
#......#.#..........#....#.#...
###................#.#....#....
#..#.##.#.............#..#.....
.....#............#.....##.....
....#.....#....#.........#.....
#..#...........###.#....#......
..#............##...#........##
..#....#..#....#.....#.......#.
..#..#.#.#.##.#..#...#.....#...
..........#..#.................
...#.#......#..##........#.....
...............#...............
#.......#.......#....#.........
#...........#....#.............
....#..#..........#....#..##...
.........#.#.#.........#......#
.....#...##.....#.#.......#...#
.........#....#...#.......#....


"""