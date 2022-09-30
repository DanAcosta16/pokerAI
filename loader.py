import json
from sys import argv

def read(fn):
	data = json.loads("{}")
	try:
		with open(fn) as file: data = json.loads(file.read())
	except Exception as e: print(e)
	return data
def write(data, fn):
	if(type(data) != type(dict()) and type(data) != type(json())): return False
	try:
		with open(fn, "w") as file: file.write(json.dumps(data, indent = 4))
		return True
	except Exception as e: print(e)
	return False
# def matchVal(val):
# 	match val:
# 		case 1: return "A"
# 		case 2: return "2"
# 		case 3: return "3"
# 		case 4: return "4"
# 		case 5: return "5"
# 		case 6: return "6"
# 		case 7: return "7"
# 		case 8: return "8"
# 		case 9: return "9"
# 		case 10: return "10"
# 		case 11: return "J"
# 		case 12: return "Q"
# 		case 13: return "K"

def matchVal(val):
	if val == 1: return "A"
	elif val == 2: return "2"
	elif val == 3: return "3"
	elif val == 4: return "4"
	elif val == 5: return "5"
	elif val == 6: return "6"
	elif val == 7: return "7"
	elif val == 8: return "8"
	elif val == 9: return "9"
	elif val == 10: return "10"
	elif val == 11: return "J"
	elif val == 12: return "Q"
	elif val == 13: return "K"

def formatStraights(l):
	straights = list()
	for s in l: straights.append(f"{s[0]},{s[1]},{s[2]}")
	return straights

data = json.loads("{}")
pairs = list()
threes = list()
straights = list()
flushes = list()
sflushes = list()
for i in range(13):
	val = matchVal(i+1)
	for k in range(1, 14):
		if(k != i+1): pairs.append(f"{val},{val},{matchVal(k)}")
	threes.append(f"{val},{val},{val}")
	if(i+2 < 13):
		localStraight = [val]
		for k in range(i+2, i+4): localStraight.append(matchVal(k))
		straights.append(localStraight)

straights.append(["Q","K","A"])
straights = formatStraights(straights)
wintypes = {
	"pair": list(),
	"three of kind": list(),
	"straight": list(),
	"flush": list(),
	"straight flush": list()
}
data["wins"] = wintypes
data["wins"]["pair"] = pairs
data["wins"]["three of kind"] = threes
data["wins"]["straight"] = straights
suits = ["S", "D", "H", "C"]
for suit in suits:
	for i in range(13):
		a = matchVal(i+1)+suit
		for k in range(i+1, 13):
			b = matchVal(k+1)+suit
			for j in range(k+1, 13):
				c = matchVal(j+1)+suit
				local = [a, b, c]
				flushes.append(",".join(local))
for s in straights:
	localStraight = list()
	for card in s.split(","): localStraight.append(card)
	for suit in suits:
		local = list()
		for card in localStraight: local.append(card+suit)
		sflushes.append(",".join(local))
		#for suit in suits:
		#	local.append(card+suit)
		#	sflushes.append(local)
data["wins"]["flush"] = flushes
data["wins"]["straight flush"] = sflushes

rankings = {
	"single": 0,
	"pair": 1,
	"flush": 2,
	"straight": 3,
	"three of kind": 4,
	"straight flush": 5
}
data["rankings"] = rankings

if(len(argv) > 1): fn = argv[1]
else: fn = "cheat.json"
write(data, fn)
#write(data, "cheat.json")
#print(str(data))
