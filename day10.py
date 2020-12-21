
# DAY 10

def joltDiff():
	inp = [0]
	for _ in range(94):
		inp.append(int(input()))
	inp.sort()
	inp.append(inp[-1]+3)
	print(inp)
	Diff1 = 0
	Diff3 = 0
	compulsory = [0]
	for i,n in enumerate(inp):
		if i in range(1,97):
			#if n-inp[i-1]==1:
				#Diff1+=1
			#elif n-inp[i-1]==3:
				#Diff3+=1
			if n-inp[i-1]==3:
				if(inp[i-1] not in compulsory):
					compulsory.append(inp[i-1])
				compulsory.append(n)
			
	print(compulsory)
	#print(Diff1,Diff3)
	#print(Diff1*Diff3)
#joltDiff()

def combinations():
	inp = [0, 1, 2, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 19, 22, 23, 24, 25, 28, 31, 34, 35, 36, 37, 38, 41, 44, 45, 46, 47, 48, 51, 54, 55, 58, 59, 60, 61, 62, 65, 66, 69, 72, 73, 74, 75, 76, 79, 80, 81, 82, 83, 86, 87, 88, 89, 90, 93, 94, 95, 96, 99, 100, 103, 106, 107, 108, 109, 112, 113, 114, 117, 120, 121, 122, 123, 124, 127, 130, 131, 132, 133, 134, 137, 140, 141, 142, 143, 144, 147, 148, 149, 150, 151, 154, 157]
	compulsory = [0, 2, 5, 9, 12, 16, 19, 22, 25, 28, 31, 34, 38, 41, 44, 48, 51, 54, 55, 58, 62, 65, 66, 69, 72, 76, 79, 83, 86, 90, 93, 96, 99, 100, 103, 106, 109, 112, 114, 117, 120, 124, 127, 130, 134, 137, 140, 144, 147, 151, 154, 157]
	print(len(inp))
	print(len(compulsory))
	#print(2*6*6*3*6*6*6*6*6*6*3*3*6*6*6*6)
	cnt = 0
	ans = 1
	for i in inp:
		print(i)
		print(cnt)
		if i not in compulsory:
			cnt+=1
		else:
			if cnt==1:
				ans*=2
			elif cnt==2:
				ans*=4
			elif cnt==3:
				ans*=7
			cnt=0
	print(ans)
combinations()

""" Input

38
23
31
16
141
2
124
25
37
147
86
150
99
75
81
121
93
120
96
55
48
58
108
22
132
62
107
54
69
51
7
134
143
122
28
60
123
82
95
14
6
106
41
131
109
90
112
1
103
44
127
9
83
59
117
8
140
151
89
35
148
76
100
114
130
19
72
36
133
12
34
46
15
45
87
144
80
13
142
149
88
94
61
154
24
66
113
5
73
79
74
65
137
47

"""
