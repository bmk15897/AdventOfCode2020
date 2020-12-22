
# DAY 22

def cardGame():
	player1Cards = []
	for i in range(25):
		player1Cards.append(int(input()))
	
	player2Cards = []
	for i in range(25):
		player2Cards.append(int(input()))
	r = 0
	while len(player1Cards)!=0 and len(player2Cards)!=0:
		r+=1
		if player1Cards[0]> player2Cards[0]:
			player1Cards.append(player1Cards.pop(0))
			player1Cards.append(player2Cards.pop(0))
		else:
			player2Cards.append(player2Cards.pop(0))
			player2Cards.append(player1Cards.pop(0))
	
	ans = 0
	if len(player1Cards)==0:
		for i,n in enumerate(player2Cards):
			ans += (50-i)*n
	else:
		for i,n in enumerate(player1Cards):
			ans += (50-i)*n
	print(ans)
	print(player1Cards)
	print(player2Cards)
	print(r)
#cardGame()



def recursiveCombat2(p1, p2):
    p1CardsPrevRound = []
    p2CardsPrevRound = []
    while len(p1)!=0 and len(p2)!=0:
        if (p1 in p1CardsPrevRound) or (p2 in p2CardsPrevRound):
            return 1, p1
        p1CardsPrevRound.append(p1)
        p2CardsPrevRound.append(p2)
        a = p1[0]
        b = p2[0]
        p1 = p1[1:]
        p2 = p2[1:]
        if a <= len(p1) and b <= len(p2):
            c_p1 = copy.deepcopy(p1)[:a]
            c_p2 = copy.deepcopy(p2)[:b]
            winner, ok = recursiveCombat2(c_p1, c_p2)
            if winner == 1:
                p1.append(a)
                p1.append(b)
            else:
                p2.append(b)
                p2.append(a)
        elif a > b:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)
    if len(p1)!=0:
        return (1, p1)
    else:
        return (2, p2)


def cardGameMain():
	player1Cards = []
	for i in range(25):
		player1Cards.append(int(input()))
	
	player2Cards = []
	for i in range(25):
		player2Cards.append(int(input()))
	
	winner, cards = recursiveCombat2(player1Cards, player2Cards)
	ans = 0
	for i,n in enumerate(cards):
		ans += (50-i)*n
	print(ans)
	
cardGameMain()


""" Input

26
16
33
8
5
46
12
47
39
27
50
10
34
20
23
11
43
14
18
1
48
28
31
38
41
45
7
9
4
15
19
49
3
36
25
24
2
21
37
35
44
29
13
32
22
17
30
42
40
6

"""