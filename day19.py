import re
# DAY 19

def grammarRules():
	rules = {}
	
	for _ in range(6):
		m = re.match("(\d*): ([0-9 \"a-z|]*)",input())
		print(m.group(1),m.group(2))
		p = m.group(2).split()
		cnt = 0
		temp = []
		rules[m.group(1)] = []
		for i in p:
			print(i)
			if i == '|':
				rules[m.group(1)].append(temp)
				temp = []
			elif i != ' ' and i!='\"':
				temp.append(i)
			cnt += 1
		rules[m.group(1)].append(temp)
	print(rules)
#grammarRules()

#children = {64: [["a"]], 14: [["b"]]}
children = {4: ["a"], 5: ["b"]}
def giveChild(r, rules):
	print(r)
	if rules[r][0][0] in ('a','b'):
		return rules[r][0][0]
	temp = []
	for i in rules[r]:
		child = []
		for j in i:
			if j in children:
				print(j,"in children")
				for k in children[j]:
					child.append(''.join(k))
			else:
				print(j,"not in children")
				e = giveChild(j,rules)
				print("e",e)
				temp9 = []
				for k in e:
					temp9.extend(k)
				child.append(''.join(temp9))
		print("child",child)
		temp.append(''.join(child))
	children[r] = temp
	print(children)
	return temp
			
			
def deriving0Rule():
	#rules = {'101': [['64', '33'], ['14', '121']], '130': [['14', '96']], '117': [['64', '14'], ['14', '14']], '48': [['78', '14'], ['102', '64']], '107': [['14', '14'], ['64', '64']], '56': [['14', '43'], ['64', '104']], '5': [['107', '14'], ['106', '64']], '67': [['14', '44'], ['64', '94']], '100': [['14', '39'], ['64', '103']], '32': [['14', '96'], ['64', '16']], '25': [['64', '107'], ['14', '96']], '37': [['64', '108'], ['14', '30']], '42': [['95', '14'], ['27', '64']], '113': [['14', '79']], '13': [['14', '136'], ['64', '116']], '83': [['64', '62'], ['14', '2']], '105': [['14', '108'], ['64', '117']], '28': [['14', '133'], ['64', '35']], '66': [['64', '106'], ['14', '96']], '41': [['64', '85'], ['14', '60']], '88': [['16', '64'], ['108', '14']], '49': [['58', '64'], ['14', '14']], '111': [['52', '64'], ['114', '14']], '3': [['14', '124'], ['64', '119']], '82': [['14', '17'], ['64', '47']], '116': [['49', '14'], ['98', '64']], '91': [['58', '6']], '127': [['106', '64'], ['30', '14']], '125': [['56', '14'], ['100', '64']], '23': [['64', '61'], ['14', '5']], '31': [['64', '9'], ['14', '109']], '86': [['125', '14'], ['99', '64']], '35': [['64', '49'], ['14', '106']], '10': [['64', '25'], ['14', '84']], '85': [['92', '64'], ['132', '14']], '46': [['14', '18'], ['64', '82']], '128': [['78', '14'], ['79', '64']], '79': [['64', '64'], ['14', '64']], '29': [['135', '14'], ['68', '64']], '87': [['106', '14'], ['79', '64']], '96': [['64', '14'], ['64', '64']], '27': [['134', '14'], ['51', '64']], '109': [['76', '64'], ['86', '14']], '9': [['64', '120'], ['14', '74']], '81': [['64', '131'], ['14', '93']], '12': [['118', '64'], ['37', '14']], '11': [['42', '31']], '108': [['64', '14'], ['14', '64']], '16': [['64', '14'], ['14', '58']], '63': [['117', '64'], ['16', '14']], '126': [['64', '129'], ['14', '15']], '53': [['64', '79'], ['14', '16']], '75': [['105', '14'], ['88', '64']], '93': [['127', '14'], ['73', '64']], '26': [['36', '14'], ['97', '64']], '124': [['30', '58']], '36': [['106', '14'], ['117', '64']], '21': [['25', '14'], ['119', '64']], '92': [['64', '96'], ['14', '102']], '131': [['64', '59'], ['14', '66']], '4': [['64', '108'], ['14', '106']], '44': [['32', '64'], ['71', '14']], '45': [['41', '14'], ['67', '64']], '94': [['119', '14'], ['110', '64']], '58': [['14'], ['64']], '38': [['14', '14']], '112': [['75', '14'], ['21', '64']], '104': [['58', '79']], '59': [['14', '16'], ['64', '98']], '114': [['14', '30'], ['64', '102']], '65': [['96', '14'], ['6', '64']], '68': [['30', '14'], ['79', '64']], '129': [['29', '14'], ['12', '64']], '39': [['14', '6'], ['64', '117']], '78': [['14', '14'], ['64', '58']], '115': [['14', '72'], ['64', '24']], '57': [['64', '122'], ['14', '22']], '71': [['107', '14'], ['96', '64']], '30': [['14', '14'], ['14', '64']], '64': [['"a"']], '106': [['14', '64']], '89': [['28', '64'], ['80', '14']], '20': [['64', '70'], ['14', '19']], '133': [['107', '14'], ['34', '64']], '34': [['64', '64']], '22': [['96', '58']], '90': [['16', '14'], ['96', '64']], '51': [['14', '46'], ['64', '112']], '69': [['23', '14'], ['13', '64']], '15': [['14', '55'], ['64', '3']], '123': [['30', '14'], ['108', '64']], '17': [['117', '64'], ['78', '14']], '40': [['49', '64'], ['117', '14']], '135': [['64', '34'], ['14', '108']], '47': [['64', '102'], ['14', '78']], '97': [['14', '34'], ['64', '117']], '2': [['64', '63'], ['14', '88']], '54': [['14', '26'], ['64', '77']], '118': [['98', '14'], ['96', '64']], '76': [['69', '14'], ['54', '64']], '102': [['64', '14']], '121': [['114', '14'], ['130', '64']], '99': [['64', '57'], ['14', '10']], '60': [['130', '64'], ['65', '14']], '98': [['58', '58']], '132': [['64', '117'], ['14', '30']], '74': [['89', '14'], ['50', '64']], '19': [['78', '64'], ['6', '14']], '1': [['115', '64'], ['20', '14']], '18': [['53', '64'], ['128', '14']], '72': [['14', '78'], ['64', '30']], '103': [['34', '64'], ['38', '14']], '52': [['30', '14'], ['49', '64']], '120': [['83', '14'], ['81', '64']], '70': [['79', '14'], ['108', '64']], '7': [['64', '113'], ['14', '40']], '24': [['49', '14'], ['16', '64']], '84': [['30', '64'], ['34', '14']], '110': [['64', '30'], ['14', '96']], '55': [['14', '90'], ['64', '37']], '62': [['14', '4'], ['64', '47']], '80': [['64', '48'], ['14', '91']], '95': [['126', '64'], ['45', '14']], '77': [['14', '87'], ['64', '35']], '14': [['"b"']], '134': [['101', '64'], ['1', '14']], '119': [['14', '102'], ['64', '102']], '0': [['8', '11']], '33': [['14', '92'], ['64', '123']], '6': [['58', '64'], ['64', '14']], '50': [['111', '64'], ['7', '14']], '43': [['14', '98'], ['64', '38']], '73': [['102', '14'], ['6', '64']], '61': [['96', '64']], '8': [['42']], '136': [['30', '64'], ['96', '14']], '122': [['58', '49']]}
	#rules = {'0': [['4', '1', '5']], '1': [['2', '3'], ['3', '2']], '2': [['4', '4'], ['5', '5']], '3': [['4', '5'], ['5', '4']], '4': [["a"]], '5': [["b"]]}
	orderRules = []
	for i in range(6):
		orderRules.append(rules[str(i)])
	print(orderRules)
	#orderRules = [[['8', '1', '1']], [['1', '1', '5', '6', '4'], ['2', '0', '1', '4']], [['6', '4', '6', '3'], ['1', '4', '8', '8']], [['1', '4', '1', '2', '4'], ['6', '4', '1', '1', '9']], [['6', '4', '1', '0', '8'], ['1', '4', '1', '0', '6']], [['1', '0', '7', '1', '4'], ['1', '0', '6', '6', '4']], [['5', '8', '6', '4'], ['6', '4', '1', '4']], [['6', '4', '1', '1', '3'], ['1', '4', '4', '0']], [['4', '2']], [['6', '4', '1', '2', '0'], ['1', '4', '7', '4']], [['6', '4', '2', '5'], ['1', '4', '8', '4']], [['4', '2', '3', '1']], [['1', '1', '8', '6', '4'], ['3', '7', '1', '4']], [['1', '4', '1', '3', '6'], ['6', '4', '1', '1', '6']], [['b']], [['1', '4', '5', '5'], ['6', '4', '3']], [['6', '4', '1', '4'], ['1', '4', '5', '8']], [['1', '1', '7', '6', '4'], ['7', '8', '1', '4']], [['5', '3', '6', '4'], ['1', '2', '8', '1', '4']], [['7', '8', '6', '4'], ['6', '1', '4']], [['6', '4', '7', '0'], ['1', '4', '1', '9']], [['2', '5', '1', '4'], ['1', '1', '9', '6', '4']], [['9', '6', '5', '8']], [['6', '4', '6', '1'], ['1', '4', '5']], [['4', '9', '1', '4'], ['1', '6', '6', '4']], [['6', '4', '1', '0', '7'], ['1', '4', '9', '6']], [['3', '6', '1', '4'], ['9', '7', '6', '4']], [['1', '3', '4', '1', '4'], ['5', '1', '6', '4']], [['1', '4', '1', '3', '3'], ['6', '4', '3', '5']], [['1', '3', '5', '1', '4'], ['6', '8', '6', '4']], [['1', '4', '1', '4'], ['1', '4', '6', '4']], [['6', '4', '9'], ['1', '4', '1', '0', '9']], [['1', '4', '9', '6'], ['6', '4', '1', '6']], [['1', '4', '9', '2'], ['6', '4', '1', '2', '3']], [['6', '4', '6', '4']], [['6', '4', '4', '9'], ['1', '4', '1', '0', '6']], [['1', '0', '6', '1', '4'], ['1', '1', '7', '6', '4']], [['6', '4', '1', '0', '8'], ['1', '4', '3', '0']], [['1', '4', '1', '4']], [['1', '4', '6'], ['6', '4', '1', '1', '7']], [['4', '9', '6', '4'], ['1', '1', '7', '1', '4']], [['6', '4', '8', '5'], ['1', '4', '6', '0']], [['9', '5', '1', '4'], ['2', '7', '6', '4']], [['1', '4', '9', '8'], ['6', '4', '3', '8']], [['3', '2', '6', '4'], ['7', '1', '1', '4']], [['4', '1', '1', '4'], ['6', '7', '6', '4']], [['1', '4', '1', '8'], ['6', '4', '8', '2']], [['6', '4', '1', '0', '2'], ['1', '4', '7', '8']], [['7', '8', '1', '4'], ['1', '0', '2', '6', '4']], [['5', '8', '6', '4'], ['1', '4', '1', '4']], [['1', '1', '1', '6', '4'], ['7', '1', '4']], [['1', '4', '4', '6'], ['6', '4', '1', '1', '2']], [['3', '0', '1', '4'], ['4', '9', '6', '4']], [['6', '4', '7', '9'], ['1', '4', '1', '6']], [['1', '4', '2', '6'], ['6', '4', '7', '7']], [['1', '4', '9', '0'], ['6', '4', '3', '7']], [['1', '4', '4', '3'], ['6', '4', '1', '0', '4']], [['6', '4', '1', '2', '2'], ['1', '4', '2', '2']], [['1', '4'], ['6', '4']], [['1', '4', '1', '6'], ['6', '4', '9', '8']], [['1', '3', '0', '6', '4'], ['6', '5', '1', '4']], [['9', '6', '6', '4']], [['1', '4', '4'], ['6', '4', '4', '7']], [['1', '1', '7', '6', '4'], ['1', '6', '1', '4']], [['a']], [['9', '6', '1', '4'], ['6', '6', '4']], [['6', '4', '1', '0', '6'], ['1', '4', '9', '6']], [['1', '4', '4', '4'], ['6', '4', '9', '4']], [['3', '0', '1', '4'], ['7', '9', '6', '4']], [['2', '3', '1', '4'], ['1', '3', '6', '4']], [['7', '9', '1', '4'], ['1', '0', '8', '6', '4']], [['1', '0', '7', '1', '4'], ['9', '6', '6', '4']], [['1', '4', '7', '8'], ['6', '4', '3', '0']], [['1', '0', '2', '1', '4'], ['6', '6', '4']], [['8', '9', '1', '4'], ['5', '0', '6', '4']], [['1', '0', '5', '1', '4'], ['8', '8', '6', '4']], [['6', '9', '1', '4'], ['5', '4', '6', '4']], [['1', '4', '8', '7'], ['6', '4', '3', '5']], [['1', '4', '1', '4'], ['6', '4', '5', '8']], [['6', '4', '6', '4'], ['1', '4', '6', '4']], [['6', '4', '4', '8'], ['1', '4', '9', '1']], [['6', '4', '1', '3', '1'], ['1', '4', '9', '3']], [['1', '4', '1', '7'], ['6', '4', '4', '7']], [['6', '4', '6', '2'], ['1', '4', '2']], [['3', '0', '6', '4'], ['3', '4', '1', '4']], [['9', '2', '6', '4'], ['1', '3', '2', '1', '4']], [['1', '2', '5', '1', '4'], ['9', '9', '6', '4']], [['1', '0', '6', '1', '4'], ['7', '9', '6', '4']], [['1', '6', '6', '4'], ['1', '0', '8', '1', '4']], [['2', '8', '6', '4'], ['8', '0', '1', '4']], [['1', '6', '1', '4'], ['9', '6', '6', '4']], [['5', '8', '6']], [['6', '4', '9', '6'], ['1', '4', '1', '0', '2']], [['1', '2', '7', '1', '4'], ['7', '3', '6', '4']], [['1', '1', '9', '1', '4'], ['1', '1', '0', '6', '4']], [['1', '2', '6', '6', '4'], ['4', '5', '1', '4']], [['6', '4', '1', '4'], ['6', '4', '6', '4']], [['1', '4', '3', '4'], ['6', '4', '1', '1', '7']], [['5', '8', '5', '8']], [['6', '4', '5', '7'], ['1', '4', '1', '0']], [['1', '4', '3', '9'], ['6', '4', '1', '0', '3']], [['6', '4', '3', '3'], ['1', '4', '1', '2', '1']], [['6', '4', '1', '4']], [['3', '4', '6', '4'], ['3', '8', '1', '4']], [['5', '8', '7', '9']], [['1', '4', '1', '0', '8'], ['6', '4', '1', '1', '7']], [['1', '4', '6', '4']], [['1', '4', '1', '4'], ['6', '4', '6', '4']], [['6', '4', '1', '4'], ['1', '4', '6', '4']], [['7', '6', '6', '4'], ['8', '6', '1', '4']], [['6', '4', '3', '0'], ['1', '4', '9', '6']], [['5', '2', '6', '4'], ['1', '1', '4', '1', '4']], [['7', '5', '1', '4'], ['2', '1', '6', '4']], [['1', '4', '7', '9']], [['1', '4', '3', '0'], ['6', '4', '1', '0', '2']], [['1', '4', '7', '2'], ['6', '4', '2', '4']], [['4', '9', '1', '4'], ['9', '8', '6', '4']], [['6', '4', '1', '4'], ['1', '4', '1', '4']], [['9', '8', '1', '4'], ['9', '6', '6', '4']], [['1', '4', '1', '0', '2'], ['6', '4', '1', '0', '2']], [['8', '3', '1', '4'], ['8', '1', '6', '4']], [['1', '1', '4', '1', '4'], ['1', '3', '0', '6', '4']], [['5', '8', '4', '9']], [['3', '0', '1', '4'], ['1', '0', '8', '6', '4']], [['3', '0', '5', '8']], [['5', '6', '1', '4'], ['1', '0', '0', '6', '4']], [['6', '4', '1', '2', '9'], ['1', '4', '1', '5']], [['1', '0', '6', '6', '4'], ['3', '0', '1', '4']], [['7', '8', '1', '4'], ['7', '9', '6', '4']], [['2', '9', '1', '4'], ['1', '2', '6', '4']], [['1', '4', '9', '6']], [['6', '4', '5', '9'], ['1', '4', '6', '6']], [['6', '4', '1', '1', '7'], ['1', '4', '3', '0']], [['1', '0', '7', '1', '4'], ['3', '4', '6', '4']], [['1', '0', '1', '6', '4'], ['1', '1', '4']], [['6', '4', '3', '4'], ['1', '4', '1', '0', '8']], [['3', '0', '6', '4'], ['9', '6', '1', '4']]]
	rules = []
	for i in orderRules:
		tempi = []
		for j in i:
			tempj = []
			for k in j:
				if k.isdigit():
					tempj.append(int(k))
				else:
					tempj.append(k)
			tempi.append(tempj)
		rules.append(tempi)
	print(rules)
	#rules = [[[8, 1, 1]], [[1, 1, 5, 6, 4], [2, 0, 1, 4]], [[6, 4, 6, 3], [1, 4, 8, 8]], [[1, 4, 1, 2, 4], [6, 4, 1, 1, 9]], [[6, 4, 1, 0, 8], [1, 4, 1, 0, 6]], [[1, 0, 7, 1, 4], [1, 0, 6, 6, 4]], [[5, 8, 6, 4], [6, 4, 1, 4]], [[6, 4, 1, 1, 3], [1, 4, 4, 0]], [[4, 2]], [[6, 4, 1, 2, 0], [1, 4, 7, 4]], [[6, 4, 2, 5], [1, 4, 8, 4]], [[4, 2, 3, 1]], [[1, 1, 8, 6, 4], [3, 7, 1, 4]], [[1, 4, 1, 3, 6], [6, 4, 1, 1, 6]], [['b']], [[1, 4, 5, 5], [6, 4, 3]], [[6, 4, 1, 4], [1, 4, 5, 8]], [[1, 1, 7, 6, 4], [7, 8, 1, 4]], [[5, 3, 6, 4], [1, 2, 8, 1, 4]], [[7, 8, 6, 4], [6, 1, 4]], [[6, 4, 7, 0], [1, 4, 1, 9]], [[2, 5, 1, 4], [1, 1, 9, 6, 4]], [[9, 6, 5, 8]], [[6, 4, 6, 1], [1, 4, 5]], [[4, 9, 1, 4], [1, 6, 6, 4]], [[6, 4, 1, 0, 7], [1, 4, 9, 6]], [[3, 6, 1, 4], [9, 7, 6, 4]], [[1, 3, 4, 1, 4], [5, 1, 6, 4]], [[1, 4, 1, 3, 3], [6, 4, 3, 5]], [[1, 3, 5, 1, 4], [6, 8, 6, 4]], [[1, 4, 1, 4], [1, 4, 6, 4]], [[6, 4, 9], [1, 4, 1, 0, 9]], [[1, 4, 9, 6], [6, 4, 1, 6]], [[1, 4, 9, 2], [6, 4, 1, 2, 3]], [[6, 4, 6, 4]], [[6, 4, 4, 9], [1, 4, 1, 0, 6]], [[1, 0, 6, 1, 4], [1, 1, 7, 6, 4]], [[6, 4, 1, 0, 8], [1, 4, 3, 0]], [[1, 4, 1, 4]], [[1, 4, 6], [6, 4, 1, 1, 7]], [[4, 9, 6, 4], [1, 1, 7, 1, 4]], [[6, 4, 8, 5], [1, 4, 6, 0]], [[9, 5, 1, 4], [2, 7, 6, 4]], [[1, 4, 9, 8], [6, 4, 3, 8]], [[3, 2, 6, 4], [7, 1, 1, 4]], [[4, 1, 1, 4], [6, 7, 6, 4]], [[1, 4, 1, 8], [6, 4, 8, 2]], [[6, 4, 1, 0, 2], [1, 4, 7, 8]], [[7, 8, 1, 4], [1, 0, 2, 6, 4]], [[5, 8, 6, 4], [1, 4, 1, 4]], [[1, 1, 1, 6, 4], [7, 1, 4]], [[1, 4, 4, 6], [6, 4, 1, 1, 2]], [[3, 0, 1, 4], [4, 9, 6, 4]], [[6, 4, 7, 9], [1, 4, 1, 6]], [[1, 4, 2, 6], [6, 4, 7, 7]], [[1, 4, 9, 0], [6, 4, 3, 7]], [[1, 4, 4, 3], [6, 4, 1, 0, 4]], [[6, 4, 1, 2, 2], [1, 4, 2, 2]], [[1, 4], [6, 4]], [[1, 4, 1, 6], [6, 4, 9, 8]], [[1, 3, 0, 6, 4], [6, 5, 1, 4]], [[9, 6, 6, 4]], [[1, 4, 4], [6, 4, 4, 7]], [[1, 1, 7, 6, 4], [1, 6, 1, 4]], [['a']], [[9, 6, 1, 4], [6, 6, 4]], [[6, 4, 1, 0, 6], [1, 4, 9, 6]], [[1, 4, 4, 4], [6, 4, 9, 4]], [[3, 0, 1, 4], [7, 9, 6, 4]], [[2, 3, 1, 4], [1, 3, 6, 4]], [[7, 9, 1, 4], [1, 0, 8, 6, 4]], [[1, 0, 7, 1, 4], [9, 6, 6, 4]], [[1, 4, 7, 8], [6, 4, 3, 0]], [[1, 0, 2, 1, 4], [6, 6, 4]], [[8, 9, 1, 4], [5, 0, 6, 4]], [[1, 0, 5, 1, 4], [8, 8, 6, 4]], [[6, 9, 1, 4], [5, 4, 6, 4]], [[1, 4, 8, 7], [6, 4, 3, 5]], [[1, 4, 1, 4], [6, 4, 5, 8]], [[6, 4, 6, 4], [1, 4, 6, 4]], [[6, 4, 4, 8], [1, 4, 9, 1]], [[6, 4, 1, 3, 1], [1, 4, 9, 3]], [[1, 4, 1, 7], [6, 4, 4, 7]], [[6, 4, 6, 2], [1, 4, 2]], [[3, 0, 6, 4], [3, 4, 1, 4]], [[9, 2, 6, 4], [1, 3, 2, 1, 4]], [[1, 2, 5, 1, 4], [9, 9, 6, 4]], [[1, 0, 6, 1, 4], [7, 9, 6, 4]], [[1, 6, 6, 4], [1, 0, 8, 1, 4]], [[2, 8, 6, 4], [8, 0, 1, 4]], [[1, 6, 1, 4], [9, 6, 6, 4]], [[5, 8, 6]], [[6, 4, 9, 6], [1, 4, 1, 0, 2]], [[1, 2, 7, 1, 4], [7, 3, 6, 4]], [[1, 1, 9, 1, 4], [1, 1, 0, 6, 4]], [[1, 2, 6, 6, 4], [4, 5, 1, 4]], [[6, 4, 1, 4], [6, 4, 6, 4]], [[1, 4, 3, 4], [6, 4, 1, 1, 7]], [[5, 8, 5, 8]], [[6, 4, 5, 7], [1, 4, 1, 0]], [[1, 4, 3, 9], [6, 4, 1, 0, 3]], [[6, 4, 3, 3], [1, 4, 1, 2, 1]], [[6, 4, 1, 4]], [[3, 4, 6, 4], [3, 8, 1, 4]], [[5, 8, 7, 9]], [[1, 4, 1, 0, 8], [6, 4, 1, 1, 7]], [[1, 4, 6, 4]], [[1, 4, 1, 4], [6, 4, 6, 4]], [[6, 4, 1, 4], [1, 4, 6, 4]], [[7, 6, 6, 4], [8, 6, 1, 4]], [[6, 4, 3, 0], [1, 4, 9, 6]], [[5, 2, 6, 4], [1, 1, 4, 1, 4]], [[7, 5, 1, 4], [2, 1, 6, 4]], [[1, 4, 7, 9]], [[1, 4, 3, 0], [6, 4, 1, 0, 2]], [[1, 4, 7, 2], [6, 4, 2, 4]], [[4, 9, 1, 4], [9, 8, 6, 4]], [[6, 4, 1, 4], [1, 4, 1, 4]], [[9, 8, 1, 4], [9, 6, 6, 4]], [[1, 4, 1, 0, 2], [6, 4, 1, 0, 2]], [[8, 3, 1, 4], [8, 1, 6, 4]], [[1, 1, 4, 1, 4], [1, 3, 0, 6, 4]], [[5, 8, 4, 9]], [[3, 0, 1, 4], [1, 0, 8, 6, 4]], [[3, 0, 5, 8]], [[5, 6, 1, 4], [1, 0, 0, 6, 4]], [[6, 4, 1, 2, 9], [1, 4, 1, 5]], [[1, 0, 6, 6, 4], [3, 0, 1, 4]], [[7, 8, 1, 4], [7, 9, 6, 4]], [[2, 9, 1, 4], [1, 2, 6, 4]], [[1, 4, 9, 6]], [[6, 4, 5, 9], [1, 4, 6, 6]], [[6, 4, 1, 1, 7], [1, 4, 3, 0]], [[1, 0, 7, 1, 4], [3, 4, 6, 4]], [[1, 0, 1, 6, 4], [1, 1, 4]], [[6, 4, 3, 4], [1, 4, 1, 0, 8]], [[3, 0, 6, 4], [9, 6, 1, 4]]]
	print(giveChild(0,rules))
	print(children)
	
	
#deriving0Rule()

import re

#use this to order the rules and replace : with ->
def grammarRules():
	rules = {}
	for _ in range(137):
		m = re.match("(\d*): ([0-9 \"a-z|]*)",input())
		rules[m.group(1)] = m.group(1)+" -> "+m.group(2)
	for i in range(137):
		print(rules[str(i)])
		
#grammarRules()
#copy paste the output of the above in myGrammar.txt and then run the below code

import nltk
grammar = nltk.CFG.fromstring(open("myGrammar.txt").readlines())
print(grammar.start())
print(grammar.productions())
ans = 0
for i in range(398):
	rd = nltk.RecursiveDescentParser(grammar)
	sentence = input()
	ok = 0
	for r in rd.parse(sentence):
		print(r)
		ok+=1
	if ok!=0:
		ans+=1
print(ans)

""" Input

101: 64 33 | 14 121
130: 14 96
117: 64 14 | 14 14
48: 78 14 | 102 64
107: 14 14 | 64 64
56: 14 43 | 64 104
5: 107 14 | 106 64
67: 14 44 | 64 94
100: 14 39 | 64 103
32: 14 96 | 64 16
25: 64 107 | 14 96
37: 64 108 | 14 30
42: 95 14 | 27 64
113: 14 79
13: 14 136 | 64 116
83: 64 62 | 14 2
105: 14 108 | 64 117
28: 14 133 | 64 35
66: 64 106 | 14 96
41: 64 85 | 14 60
88: 16 64 | 108 14
49: 58 64 | 14 14
111: 52 64 | 114 14
3: 14 124 | 64 119
82: 14 17 | 64 47
116: 49 14 | 98 64
91: 58 6
127: 106 64 | 30 14
125: 56 14 | 100 64
23: 64 61 | 14 5
31: 64 9 | 14 109
86: 125 14 | 99 64
35: 64 49 | 14 106
10: 64 25 | 14 84
85: 92 64 | 132 14
46: 14 18 | 64 82
128: 78 14 | 79 64
79: 64 64 | 14 64
29: 135 14 | 68 64
87: 106 14 | 79 64
96: 64 14 | 64 64
27: 134 14 | 51 64
109: 76 64 | 86 14
9: 64 120 | 14 74
81: 64 131 | 14 93
12: 118 64 | 37 14
11: 42 31
108: 64 14 | 14 64
16: 64 14 | 14 58
63: 117 64 | 16 14
126: 64 129 | 14 15
53: 64 79 | 14 16
75: 105 14 | 88 64
93: 127 14 | 73 64
26: 36 14 | 97 64
124: 30 58
36: 106 14 | 117 64
21: 25 14 | 119 64
92: 64 96 | 14 102
131: 64 59 | 14 66
4: 64 108 | 14 106
44: 32 64 | 71 14
45: 41 14 | 67 64
94: 119 14 | 110 64
58: 14 | 64
38: 14 14
112: 75 14 | 21 64
104: 58 79
59: 14 16 | 64 98
114: 14 30 | 64 102
65: 96 14 | 6 64
68: 30 14 | 79 64
129: 29 14 | 12 64
39: 14 6 | 64 117
78: 14 14 | 64 58
115: 14 72 | 64 24
57: 64 122 | 14 22
71: 107 14 | 96 64
30: 14 14 | 14 64
64: "a"
106: 14 64
89: 28 64 | 80 14
20: 64 70 | 14 19
133: 107 14 | 34 64
34: 64 64
22: 96 58
90: 16 14 | 96 64
51: 14 46 | 64 112
69: 23 14 | 13 64
15: 14 55 | 64 3
123: 30 14 | 108 64
17: 117 64 | 78 14
40: 49 64 | 117 14
135: 64 34 | 14 108
47: 64 102 | 14 78
97: 14 34 | 64 117
2: 64 63 | 14 88
54: 14 26 | 64 77
118: 98 14 | 96 64
76: 69 14 | 54 64
102: 64 14
121: 114 14 | 130 64
99: 64 57 | 14 10
60: 130 64 | 65 14
98: 58 58
132: 64 117 | 14 30
74: 89 14 | 50 64
19: 78 64 | 6 14
1: 115 64 | 20 14
18: 53 64 | 128 14
72: 14 78 | 64 30
103: 34 64 | 38 14
52: 30 14 | 49 64
120: 83 14 | 81 64
70: 79 14 | 108 64
7: 64 113 | 14 40
24: 49 14 | 16 64
84: 30 64 | 34 14
110: 64 30 | 14 96
55: 14 90 | 64 37
62: 14 4 | 64 47
80: 64 48 | 14 91
95: 126 64 | 45 14
77: 14 87 | 64 35
14: "b"
134: 101 64 | 1 14
119: 14 102 | 64 102
0: 8 11
33: 14 92 | 64 123
6: 58 64 | 64 14
50: 111 64 | 7 14
43: 14 98 | 64 38
73: 102 14 | 6 64
61: 96 64
8: 42
136: 30 64 | 96 14
122: 58 49

ababbbaaabbbbbbbbaaaabaaabbabaabbaaababbabbbbbbaabbbbbbababbaaaa
aabaabaaabbabaaaabbbabbbbbbbaababbababaa
baaabbbabbababbbbaaabbab
babbbaabbabbbbbbbbabbbababbbaaaa
baabbaabbabbabbaabbbabababbabaaa
ababbbabaaaaaaababbabaabaabbaaaa
abbabbaaaabbbaaababbababbbbbbabbbbaaabbaaababbbb
bbbaabaababaaabbbabaaabbbbaaaabaabaaaaabaaababaa
ababaabbbaababaabbababbabbaabaabaabbababbbbababb
bbaaaaaabbbbabbabaaababbabaababbaaaabaab
bbaaaabaaaababbbbabbbbaababaabbaababbabbbabbababbbababaa
bbabbbbabbbabaabaabbbbba
aaabaaabaaabbbbabaaaababbbbaaaaa
bbaabbaabbbbbbaaabababbbaabaaabaabaabbbbbabbaababbbbbbaaabbbabaaababbaabbbbbaabbbbaababababaabaa
bbbbbabaabababbaaaaabbbb
ababababbbaaaaaaaababababbbaaabaabbbbbaa
aaabbabbaaaaababbaabaaaabaaababbbabaabbb
bbaaabbaababaaaaabababababbbababbabbbbabaaabbaaaabbbabaa
ababababbabaabaabaaababbbbabbbaabaabababaaaaaabb
aaabbbbaabbbaaabbbabbbababbababaaabababaabbbaaaababbaaaababaaaaabaaabaab
abababababbabaababababababbaaaababbaaaaa
aaabbaabbbbbbaaabaaaaaaa
abbaabbaabbababaabbaaaab
baaababbababbaaaababaabababbaaaaaabaabab
baabbabbababbbbbaaabbbbbbaaabaaabaaaabbbbbbababaaabbbabbbbababababbbaabb
baaabbbbababaaaaabbaaaab
bbababbaaaabbbbaabbaaaba
baababaabaabbbbbabaabbbabbbbababbaaabaaabbbbaabaaabbabab
bbabaabababbaaabaaaaaaabbabaaaaaaabaaaaa
baabbabaaabbbbaabbbbaaab
aabaabbabbabbaabbaabbbaaabaabbbbbbabbaba
baaabbbbababbaaaaabaabbabaabbabaabaaaaabaaabbaaaaabbabbbaabbabbbbaaaaabb
baaababbbbabbbaabbababbbaaabbabbaabbbbaabbbabbaabbbbabbb
ababbaaababababbaabbbababaabbbbbababbabbaababbbbaaaaaabbaaaaabba
aaabbaabaaabbbbabbbbaaaaababbbbb
baabbaababbaaaabbaaabbaa
bbbababababbbaaabbbaabab
bbaaabaabbaaababbbbbabbb
abababbabbabbaabaabbbabb
bbaaaaaaaababababaaaaaaa
aabaaabbbabbbbaaabbaabbaaabbbababbababab
babaaababbabbaaaabbaabbb
babababbbabaaabbbaaaaaab
ababbabbabaaabbabbbbbbbb
babbbbabaabaaabbbaaaabababbbabbbabbaaaba
bbaaaabbbbaabbbbbbbbaaab
bbbaaabbbaaaaaaabababaababaabbab
aabaabbababaaaabbbbbbbbbbbbbaabbbbbaabababbbababbabbaaabaabaabbaaabbbababbbbbbbbbaabbbaaabbbabba
abaabbbaaaababbaabbaabaabababbbabaabbabaaabbabaabbababaa
aaabbbbbbabaabbaabbaaaaa
bbabbbbababbababbaabbababaabbabbabbbbbbbabbaaabaababbaab
bababbbaaababbbabbaaabababbbaaba
abbababaaaababbbaaabbabbbbababbbbbababab
bababaaabbbbbabaabaaabbabbbabbbabbbbabbabaabbbbaaabbbbab
baaababbaaabbbaababbbbbaaaaabbbbbabbbabb
bbbbbbabbaaabbaababaaaaaababaaba
aabbaaababbbbaabbbaababb
aaabbabbaabaaabbaaaaaaba
ababbaaaabbaabbabaabbbab
aaaabbababaabbabbabaababbbaaaaabbbabbabbbbaababb
bbaaabaabbaaabbabbabbbaaabbbabbabaaaabaa
aaabaaabbaaaabaaaabaabbb
ababbbbaabababaaabbaabbaabaabbbaabbbaababbbbbbbaaabbabab
bbabbbaaabababaabbbbbbabbabbbbbbabbbbaba
abbabaabbbbaaaabababbaab
aaabbbaabbaaabbabbbbababaabaabbaabaabbaa
baaaababbbbbbbabaababbbaaaaabbbb
baababababbabbbbaaaabbbb
bbbbbaaaaaaabbabaaaabbba
bbbbabbababababbbabbbbaabababbbaabaaabbb
bbaaabbbabbbaaabbbbbbaab
bbababbabababbbbbbababbbaabbaaabbabaabaaaabaaaabaabbaaaa
abbabaabbabbaabbbabbaaabbbbbbaaaabaababbaaabaaaababbaabb
babbbbbbbbbbaaabaabbbbabaabbabbababbbabaabababba
bbbabbbabbaaabaaabbaabbabbbaaaba
abbabbaaaabaabbaababbbbaaababbabbbaabbba
abbabbababababbaabbbbaba
babbbaabaaabbbaaabaabbab
aaaaababaaababbaaabbbbaabaabbbaabaaababbbbaabbbabbbabbaaabaaabbb
abaaabaabbaaabbaabbaabaabbbbaaab
abaabaaabbabbbaaaababaabbababbbbabaabbab
abaaaabbaaaabbabaaaababb
aaabbaabbbaabbbbaabaabab
bbabaabaabaaaabababbaaaa
ababbbaaababbbaaaabaabbaaabaaabbaaabbaabbaabbbbabbbbaabbabbaaaaa
bababbbbababababbbaaaabaabbbbabb
abaaaaaabaaaabaaababbaaaaaabbbbaabbbaaab
abababbbbabaaabbbaaaaabb
bbbbbbaababbbaaabbbaabaababbbbabbbababbabbabbabbbbbaaaaa
bbababbbbaaababbaaabbbaabbbbaaaababbbbaaaaaabaabaabaabbbaababbaa
abaaabbabbaabaabaabbaaaa
abaababbbbaaaaabbbbaabbababababa
baabbbaaabaabbbabbaabbab
babbbbbaabbabbbbbabbaabbaabbbbbaaabbaaaa
babababbbbbabbbabbbbbbbb
ababbbabaabaaabaabaabbab
babbababbaaabbbbaaaabbaa
abbabbbbbbabbbabaaabbaba
aaabbbaababbbaaabaabbbaabbbaaaabaababbaa
aabaaaababaaabaaaababbbabbbabababbbaabbb
baaaabbbaabbabaaababbababbaaabbbaaaabababaaaabbbbabbaabbaabbaabbabbababb
aaabbbaaaaabbabbababbbbabababbbababababa
bbaabaabbbababbaaabbbabb
ababababbbabaabbababbbbaabbbbbaa
abbaaaabaaaababbabbababb
abbbababababbbaaabaaababaaaaaaabaaabbabbabbbaaaabaabbaaabbbaabab
aababababaaaababbabbabbb
babbbbabbabbbbabbbaaabbbaaabaababbaabaabbbbaaabaabbaababaaaaaabb
aaabbbaabaaabbbabbbbabbb
ababaabbaaabaaabbbbabbabaabbabab
ababbabbabaababaababbbbaabbbabaa
abbbbaababbabbababbaaabb
ababbbababbababaabbaabaabbabbbaabbababaa
abbbaaabbbaabaaabbbbbaabbaaaaabb
abbbabbababaaabaaabbbabb
bbbaabaabaabbbbabbbabaabbbababbaaaaaabbbabbabbbbbaaabbabaaabbbab
baabbbaabbbbbbababaaababaaaaabaaaabbbaabbaaaaababbbabbaabaaaaabb
aaaaaaabbaababaabbabbbabbababbbababbabaaabbbbabaabaabbbb
bababbaaaabaaabbbabaabbaabababbaaaaababa
abbabbbbaabababababbaaaa
aababbbabbaaaabababaabbb
bbbbbabbbaababababaaaaaa
babbababaabaabbbaabaabbabbababbbbaabaaabaaabbabbabaabbab
bababaaaabbbabbaaaaababb
aabaabaabbabbbbababababbabbabababaababba
ababbbabbabbababbbbbaaba
abaabababbaaabaaaaabaabb
abbabbabbbbbbaaabaabbbaaaababbbabbbaaaaa
abaaaabbbabbababbaaaaaba
bbabbaaababbbbabaaababaaabaaabbbabaababbaaabaabbaaabbbbb
aaabaabaababbbabaaabbbaaaaabbaaa
babbbbbaaaabbbaaaaabbbaabaabbabaababbbaa
babbbbabbbbbababaabaabaababbbababbbaaabb
baabbabaabaabbbaababbabbaaababbbbbbabbaabaaabbaa
abbabbaaaaabbbbabbabababaababbabbbbabbaa
aaaababababbbaaaaaababbbaaabaabaaabaabbabbaaabaa
baabaabbabbaabaabbbabbbabbaaabababaabbab
aabbaabbaabbbabaabbbbbaa
abbabbbbaaaabbabaabaaababbbabbbb
bbabbbbabbbaabaabbaaaabaaabbaaaa
abaaaababaaaabbabbbaaabababababaabaababb
babbbbbabbabababbbbbaabbbbababaaabbbabaaabbbaababbaaaaba
abbbabbabbbaabaaabaabbbb
babbbaabbababbaabbaaabba
bbaaabbaaabbaaabbbbabbbabaaaabbbaabbbbaaababaaabbbaaabbb
aaaaabbbabaabaaaabababbbabbbaabb
bbabbbabbababbbaabababaabbababbabbbababababaaaaaaaaabaababbaaabb
ababbabbbaaabbbbbabaabaabaabbbaababbabbb
bbbbbbaabbaaaabaabbabaabbbbaaaababbaababaaaabbbbbbaabbba
babaabbabaabbbbbababbbabababbbaabbbaaaaa
ababaaaaabbbbaabbaababbb
bbaaabbbbbbaabaaaabbbbba
bbbbbabbaaaaabbbababbbbaabaabababbabaaaaababbaaabbbaaababaaaabbaabbbbbab
babbaabbbababbbbbabaabbaaabaaabbbaabaaab
aabbbaaabaaababbaaaaaaababbbabaa
ababaaabaaabbbaabaabbaaa
bbbbbbaaaaabaaaaaababababbbababababababa
aaabaabaabaaabbaaaaaaaaa
babaabaaaabbaaabaaabbbaabbbbbbababbaabbb
abbabaabaabbaaabbbbbaaba
aabaaaababbabbbbabaaabababaabaab
bbabbbabbababbaabababbbaaaaaabba
aaababbabbaaabbaaaaaabbbbabbabbaabaabbbabbaabbabbbbbbaab
aaaabaaabbaaabbaaaaabaaaababbbaabbbbbabbbaabababbbabbaaaaaabaabbaabababb
bbbabaabbaabababaaaabbabbaaababbbbabbabb
babbbbaabaabaabbbbabbbaaabbaaaababbbbabb
ababaaaabbbbbabaabaababb
bbaabaabbbbabaaaababbaab
aabaaaabaababaabbaaabbaa
aaabaaaabbbbbabbaababababbbbaabb
babbbaaaabababaaababbaaabbaaabaaaabaabababaabaab
bababbbbaaabaaaaabbbaaabaabaabbb
abbbabbabaabaabbaaaaabba
baaababbbbaaabaabbabaabbabababbabababababbbbababaaabaaaa
bbabbbbababbbbbbbabbbaba
bbbbbabbbbababbbbbbbaaba
babbaabbbbabbbabbbbababb
bbaabaaabbbbbababababababbaabbaaabaaaabbbabbbaababaabbbbaaababab
ababbbabbbabbbbabaabbaab
bbaabbbbbababbaaabbaabab
aaabbaaaaaabbabbbabbbbbbabaabbbaaaaaaaaabbaabababbababaabbaababbabaaaabbaaaabaabbbbbbaab
abaaabbbbaaabbaababbbabbabbabbba
abaabbbababbbbabaababbab
abaaaabaabbabbaaaabaabab
aaabaabaaaabbbbbaabaabaaaaabbbaababbababbbbbbaab
ababaabbabaaabbaababbaba
baabbabbaaabbaabbbbaaaababbbbabaaababbbb
baaaababaaabbbbaaabbaaba
bbabbaababaaabbabbbaaaabbbaabbbababaabbb
aabaabaababababbaaabbbab
aababaabbbabaaaaaabbbbab
babbbbbaababbbaaaaaaabba
bbababbababbbaabbbabbabb
bbbaaaabbbababbabbaaababbabaaaba
bbababbbbbbbababaababaaa
babaaabbababaaaabababbaabbbaabab
ababaaaaabaaaabbababbabbbaaaaababaaaaabb
bbbbabbabbbbbabbbaaaaaaa
ababbbabbbaabaabbaaabaaa
baabbbaaaabbbbaaabbbbabb
bbaaabaabaaabbbbabababbbaabababababbaabbbbbababbabaaabbb
abbbaaababbbbbbbbabaabbb
ababaabbbbbbbbababbbbabbaabaaaabaaabbaabaaabbababbababab
abbaabaaaabbbbaaaabbabbb
bbaaabbbbbbbbbaaabbabbbbbabbbbaabaaaabbabbbaaabb
bbbabababbbbbbabbaabaabbbabbaabbbaabaabbabaabaab
bbbaaaabbaaababbabbabbbbabaabbaaabbbabbb
abbaabbabaabbaaababababaabbbaaba
babbbbbababbbaaababababa
abbbbaabaaaaababbabaaabbbaaabaab
aaabbabbbbbabaababbaaaaa
aaabbbbaabbaabbaaaaaaabb
babbaabbbbaaabababaaaabaaababbbaabbbaababbbabbaabaaaabbabaabaaabbbbaaaba
aababaabbabbbbaabbbababababbaaaa
abababaabbaaaabaababbbbb
bbbbababbbabbbbabaaababa
bbababbbaababababbbaabaaabababaabaaabbbbbaaaaaab
baabbbabbbaabbbaabbababbbbbaaabbbabbaaabbabbaabaabbbbbabababbbab
bbbbbabbbabbbbbbaabaabbb
abbabaabababaabbababbaba
abaaabaaabbabbbbababbaaaaaaaaabbaabbbabb
bbabbaabbbbbabbababbaaba
bbababbaaabababaaaaababa
baabbbaababaaabbabbbabbaaabbbabbabaaabbb
aaabbabbababbaaabbbabaababbaaabb
abbbbaabaabaabbababbbaabaaaaaaabaabbaabbabbabbba
babbabababaaaabbbabbaabbbbaaabbaabaababb
abbabbaabbbabaaaaabbbaab
babbaabbbbbbababaaababab
aaabaaaaaabbbbbbbaabababaaaaaaba
abbabbaababbababaabbbabb
abababaabbbabababbaaaabb
aaaaabbbbbbbbabaabbaaaab
bbabaababababaaabbaaabaababababa
aababaabbbaabbaababbbbbaaabbbbbaaabbabab
ababaabbbababbabbaaabaaaabaabaabaabbbbabbbbbbbbbabaabbaa
abbababaabaaababbaabbbaababbaabbbabbbabbbaababbb
bbababbabababbaaababbabbaabbaaababbaabab
aabbbaaababbaaabbbbaaaaa
babbbbaabbbabaababbbbaabbbaaaaaabbababbbaaababbabaaaaaba
bababaaaaabaabbaaabbaaaa
babbababbabbaabbbaabbbbbbbaaababbbabaababbabaaaabbbbaaabaaaabaab
aaaabaaaaaaabaaababbbaababbbbaba
baaaaabaaabbaabaaaaabaabaababbbb
bbbbbabaababbbababaabbbaabaabbbbbabbaaba
babbbbbbaaaaababbbbbababaabaaabbbaaababbaabbabbb
abaaaabaabbbbbbbbabaaaab
bababbbabbaaaaaaaaababab
abbabbabbbababbabbabbaabbaabaaaabbaababbbabaaaba
bbbbababbabababbabbabbabbbaaabaabbabbabb
aabaaabaabbabbabbaaaabaabbbbaaaabbaaabbbaaaaaabb
bbabbbabaabbbaaaababbbbabbbbbbbb
bbaaabbbbabbbbbaabbbaaaa
bbbbbabaaabaabbaaabbbbba
aaabbbbbbbbaabaaabbbbabb
baabbabbbaabbbbaaabaaabbababababbaaababa
aaaabaaaaabbbbbbababababbbbbaaba
baabbbbabaaaababababbbbababbbbba
babbaabbaaabbbbbbbbaabab
abaaaabbbaabbabaabbbaaababbabaabbaaaabbbaaabbaaaababbaab
bbaabaabbaabbbaabaabbabbbbbaabaabbbbaaabbbbaaaba
abbbababbbbabaaaaaaabbba
aabbbbbbbabbbbaaabaaabbb
bbaaaaaabbbbabbabaabbaaa
baaaabababaaabaaabaabaaabababaab
abaaabaaabbbababbbbababb
bbbabaaabaabaaaabbabbbbabbababbbbbbbaabaaabbbabb
bbaaaaabbbbaabbbbbabbabbbbababbaaaaaaabbbbbbababbaaabbbabbaabaabbaaaaaabbbbbaaba
abbaabbabaabbababaaaabababbaaabbabaaaaab
abbaabaaabaabbbabbabaaab
baabbbaabbbbbaabababaaaababbaabbabaaaaaaabbbbabbbaabaaaaabababbb
aabbaaabbbaaaabbaaaabbabaabbbaaaaabaababbbababab
baabbbbaabaaabaaabbaabbbbbaababababbaaba
abaabaaaababaaaaabaabaab
bbbbabbabbabaaaabaabbabababbbaababbbaabaabbbaaaa
abaaababaabaaabbbbbbbaaababaaaaa
ababbaaabbbbbabbaabaaaababaaabbb
aababbbbbababbaaaabbbabbabbbabababbbbbababaabaabaabbbaabaaabbbbb
babbbbbbaabaaabaabbababaabbbabbaababbbabababaabbbbbaaaba
bbbabaabbbaaaabbbbbababb
abbbabbaabaababaabbbbbbbbbababaa
aaaaabbbabbbbaabaaaabbaa
bababbbaabbabbbbaaabbbbbaabbabababbabbababaabbbbababbbbb
bbababbbabbabbbbbbabbbababaaaababbbbaaaabbbbbabbbbbbaabb
abbbababaabbaabbbbbaabab
aaababbabbbaabaaaaabbbbbabbbabbaabbababaabbbbbba
aaabbabbaababaabbababbbabbaabbbbabbbbbbbbaaabaaa
bbbbabbabbaabaabbaaabbbbbaabbabbbaababbbabaaaaaa
baabaabbbababbbbabaaabbbabaabaababbabbaaaabbbabaaaababbbbaaaabaa
bbabbaabbabbbbabababbbaabbabbaaabbbaabbb
ababaabbababbbbabbbabbbb
abababbabababbbbbbbababb
bababbbbbbbbbbaaaabaabbb
babbbbaabaabbabbbbbabbbb
baabbbbbbabbbbbbbbababab
bbbbabbababbbbbaaabbbbaaabbbbbaa
abababbabbbaaaaaaaabbbababababaaabbbababaaababbababbabbaaaabbaabaabbaababbbbaaba
abbaabaababbbbbbbaaaabba
abaabababbababbbabbbaaaa
bbbbbababbaaaabbaabbaaba
aaabbaabbaabbbaabbababaa
bbaaaabbabbabbbbaaababaa
bbbabaababaabbbbaababaaa
bbaaabbbaabaaababbbabbabbbbbbbbb
abbaabababbbbbbbbababbaabbbbabbbbabbbabaaabaabaa
bbbbbaaaaaaaababaaaaababbaababaabbbbaaabbababbab
bbaabbbbaabbbbaaabaaabaaaaabbabbaaaaabba
baabbbbabaabbabababbabaa
aabaabaabaaaabaabaabbbaaaaabaaababbbbbbbbbaabaab
ababbbaaaaabbbbbaabbbbbbbbbabbaaababbaab
babaabbaaaaabaaababbbbbababbbaabbababaab
baabababababbbaababababbbbbaabab
abaabababaabbabaaaaaaabaababbbbaaaaaaabaabbbbabaaaaaabbababbabbababaabbababbbaaa
babababbaaabaabababababa
aaababbbaababababbbbaaaaaaababbaabbbbbabaabaabbb
aababababbaabbbbbabbaabbbbbaaaaa
abaaabbaabbababababbaaababaabbab
aaabbaabbabbbbaaaabaabaabaaabbbbabbabbaabaabaaababbaaaab
bababbbbaaabbabbabaaaabbaaaabbbaabbabbbaaaabaabb
bbbabaaaaaabaaabaabbaabbbaaabaaa
babaabbabbbbababbbabaaaaabbaaabbaaaaaaaa
abbbbbbbbbaabbbbbbbaabab
ababbabbbbaaabbaaaaababb
abbbababbbaaaabbabababaaababaaabbaabaaabaaababaabaababbb
babbbbbbbababbaababababa
babaaabbbaaaabaaaaaaaaba
bbbabbbaaaababbbaaaababb
aaabaaabbbabaaaababbbaba
baabbbaaaaaabaaaaabababaaaabaabababaabbb
abbabbbbbaababaabaabbbab
bbbababbbbbabbabaababbbaabaabbbababbbbbbbbababbabbaabbabaaabaabaabaabaababaaaababbbaabaaaaaabbbb
baaabbbabababbbbbabbaaaaaaababaa
bbbaabaaaaababbbabbbabbaaaaaaabababaaaab
ababbbaabbbaabaaaaaaaaaa
baabaaaaababaabbabbbbbaa
aabbbaaaaaabbaabaabbbaaaabaabbaa
baababaaaaaabbabbbbabaababaabaab
abbbbabbaaabbabaabbbbabbbababbab
bbaaabbbabbabbaabbbaaabb
bbaaababaabaaaabaaabbbab
aaababbbaaaabbabbaaaabba
bbbbbbbbbbabaaaababbbbabaaabbabbaaaaabaabbabbbaabaabaabb
abbbababbbbbbabbabbbbaaa
aaaabaaaaabbaabbbaabbabbaaabaababbaabaabbabaaaaa
babababbaabbaabbbbbabaababbbbaabbbababab
abaaabaaabbbbbbbaababababbaabbbabaaababa
bbaabbbbabbabbabbbaaabbabbaaaaaaaabaaabbbbababaaabaaaabbbabbababbbbbaabbbbaababb
baabbbbbabbbabababbbababbbaaababbbabaabbbbaaabaaaaabbabaaaaaaabb
ababbbaabaabbabbaaabbbbbbababaaababaaaba
aaaaababbbaabbababbaabbbbbabaaabbaaabbab
aabbaabbaaaabaaaaabbbbaaabaabaaababaabbabaabbaabababbbbb
aaabbbbaaaaabaaabbbbabbabbbaababbbaabaaa
bbbbbbabbaabaaaabbbaaaaa
babbbaaabaaaabaabbbbbaabbbbbaabb
bbaabbbbbaabaaaaabbbaaaa
bbababbaaababbbaababbaaaaaaaabba
abababaabaabbbaababababbbaaaaaba
ababaaabbbaabbbbbabbaaba
abaaabbaaabbbbbbbabaabbb
aabbbbaabbaaaabbbabbbbbbaabaaababaabaababaaabbab
ababaaabababbbbaaabbbbab
abbbababbbbabaabbbbaabbb
aabbabaabaabbabbbbbbababababababaabbbabb
bababbaaaaabaabaaabbbbaaaabbabab
bbabaaaaaababbbaabbaaaaa
bababaaabbbbaaaaababaaaababbbabaabbaaaab
bbbbbaaababbbbbbabbbbbba
baabaabbbaaaabbabbbaabbaababbaab
aabbbbbbaaababbaabaaababababaaabbbbaabbaaaaaaabaaaababaa
bbbbbabbabbabaabbaaabbbbabaababaaababbabbabbabaa
aaabbabbabababaabaabaaba
abaaabbabbabbbbabaababbb
baaabbbbbbabaaaaaaaabbbb
baabaaaabaabbabaababbbabbabbabaa
babbababbbaabaabbbbbbabbaababbbb
aaabbbaabaabbbbbabbbbbab
baababbaabbbbbaaaabaabab
bbabbbababbaabaaaaaabaaaabaababababbbaabbbabbaba
ababbbbabaabbabaababbaab
ababbbaabbbbbabaaabbbaaaaabbbbbabbaabbba
babbaaababaabababbbbabaa
baabaabbbbbbabbabbaabbaaabaabbab
aabbaaabbbaaabababbaabaaabbbabababbaaabbbabbbabb
bababbbababbbaaabbbbbababbaabbaabbbbaabb
baabbbbbbaaaabaaabbbaaabbabbbbaaababbabbaaabaaaaaaaaabaaabbabaaaaabbbaabbbabbbbb
babababbabbabbbbbabbbbab
baaaababbbbabbabbbabaabaaabbbbba
babbbbabaabbaaababaaababaaabbabbbabaaababaaaaaaa
aabaaabaabbabbaaabbbbbaa
bababaaabaababaababaaaaa
ababbbbabbabaabaababaaaabaaaaabb
bbababbaabaabbbabbabbabb
baaaababbbbaabbbbbbbabaaababbaba
aaabaaabbabaabbaababbbabbaaabbaa
babaabbabbbbabbaabbabababbbbbaababbbabbb
bababbaababbbbaabbbabaaaababbababbbbabbb
bbbbbababababbaaabbabbaabbabbaabbaaabbbabaaabababaaabababbbababb
aabbbbbbbababaaaabaaaabbbbbaabba

"""