import pydealer, random, os, sys
from json import loads, dumps

class Game:
	def __winningsCheck(self):
		weight = random.randint(0, 100)
		if(self.__winnings <= 0 and weight < 66 or self.__winnings < self.player.bank_balance and weight < 33): return True
		return False
	def __newDeck(self): self.deck = pydealer.Deck()
	def __init__(self):
		self.deck = pydealer.Deck()
		self.player = Entity(self.deck, "Player")
		self.computer = Entity(self.deck, "Computer")
		self.pot = 0
		self.__consecutive = 0 # how many wins in a row
		self.__winCount = 0 # how many wins total
		self.__winnings = 0 # winnings/losses total
		self.__cheatData = readFile("cheat.json", "json")
	def shuffle(self): self.deck.shuffle()
	def increasePot(self, amount): self.pot = self.pot + amount
	def determineCheat(self):
		weight = random.randint(0, 100)
		self.__newDeck()
		if((weight < 50 and self.__consecutive == 0 or self.__consecutive == 1) or (weight < 35 and self.__consecutive == 2) or (weight < 20 and self.__consecutive == 3) or (weight < 10 and self.__consecutive == 4) or (weight < 5 and self.__consecutive >= 5) or self.__winningsCheck()):
			# cheat yes
			winTypes = ["pair", "three of kind", "straight", "flush", "straight flush"]
			winType = random.choice(winTypes)
			print(f"cheating -- chosen win type: {winType}")
			for item in self.__cheatData["wins"]: print(f"win type: {item}")
			possibleHands = self.__cheatData["wins"][winType]
			#with open("test.output", "w") as file: file.write(dumps(possibleHands, indent = 4))
			#sys.exit()
			self.computer.hand = self.deck.get_list(random.choice(possibleHands))
			self.player.dealCards() # computer can still randomly lose
		else:
			# cheat no
			self.player.dealCards()
			self.computer.dealCards()
		return

class Entity:
	def __init__(self, deck, name):
		self.deck = deck
		self.bank_balance = 200
		self.hand = pydealer.Stack()
		self.name = name
	def swapHand(self, hand): self.hand = hand
	def bet(self, amount): self.bank_balance = self.bank_balance - amount
	def dealCards(self): self.hand += self.deck.deal(3)
	def betPrompt(self):
		amount = input("Bank Balance: $" + str(self.bank_balance) + " How much would you like to bet?: ")
		value = int(amount)
		while value > self.bank_balance or value < 5: amount = input("Invalid amount. Please enter a number less than your balance and more than 5. Bank Balance: $" + str(self.bank_balance) + ". ")
		value = int(amount)
		return value
	def bet(self, amount):
		if self.name == "Player": self.bank_balance -= amount
		game.increasePot(amount)
	def callOrRaise(self, amount):
		call = 0
		random_number = random.randint(1, 10)
		print(random_number)
		if random_number < 6:
			game.computer.bet(amount)
			print("Computer calls. Pot: $" + str(game.pot))
			return call
		else:
			if game.player.bank_balance < 25: bet_raise = game.player.bank_balance
			else: bet_raise = 25
		game.computer.bet(amount + bet_raise)
		print("Computer raises $" + str(bet_raise) + ". Pot: $" + str(game.pot))
		return bet_raise

	def checkOrBet(self, amount):
		check = 0
		random_number = random.randint(1, 10)
		if random_number < 6:
			if game.player.bank_balance < 25: bet = game.player.bank_balance
			else:
				bet = 25
				game.computer.bet(bet)
				print("Computer bets $" + str(bet) + ". Pot: $" + str(game.pot))
				return bet
		else:
		    print("Computer checks.")
		    return check
	def computerChoice(self, amount):
		if amount > 0:
			choice = self.callOrRaise(amount)
			return choice
		else:
			choice = self.checkOrBet(amount)
			return choice
	def callOrFold(self, amount):
		call = 0
		fold = 1
		while True:
			ans = input("Bank balance: " + str(self.bank_balance) + ". Would you like to call or fold? Type C for call or F for fold: ")
			if ans.lower() not in ('c', 'f'): print("Invalid input. Please enter C for call or F for fold: ")
			else: break
		if ans.lower() == 'c':
			self.bet(amount)
			print(str(self.name) + " bet placed.")
			return call
		else:
			print("Player folded. Computer wins!")
			return fold

	def flop(self):
		self.showCard(0)
		self.showCard(1)
	def river(self): self.showCard(2)
	def showSuit(self, suit):
		if suit == "Hearts": return "\u2665"
		elif suit == "Diamonds": return "\u2666"
		elif suit == "Spades": return "\u2660"
		elif suit == "Clubs": return "\u2663"
	def showCard(self, index): print(self.hand[index].value + " " + self.showSuit(self.hand[index].suit))

# general purpose file reader -- defaults to text if no filetype passed
def readFile(fn, filetype = None):
	# we can add more file types if we need to for some reason
	if filetype is None: filetype = "text"
	data = None
	try:
		with open(fn) as file:
			if(filetype != "json"): data = file.read()
			else: data = loads(file.read())
	except Exception as e: print(e)
	return data



game = Game()
game.shuffle()
if(not os.path.isfile("cheat.json")):
	if sys.platform in {"win32", "cygwin", "msys"}: os.system("python loader.py")
	else: os.system("python3 loader.py")

# amount = input("Bank Balance: " + str(game.player.bank_balance) + " How much would you like to bet?: ")
# value = int(amount)
# while value > game.player.bank_balance or value < 100:
#     amount = input("Invalid amount. Please enter a number less than your balance and more than 100. Bank Balance: " + str(game.player.bank_balance) + " ")
#     value = int(amount)
amount = game.player.betPrompt()
game.player.bet(amount)
print("Player bet placed.")
game.computer.bet(amount)
print("Computer calls. Pot: $" + str(game.pot))
game.determineCheat()

"""
game.player.dealCards()
game.computer.dealCards()
"""

print("****THE FLOP****\n" + "Your hand: ")
game.player.flop()
print("Computer's hand: ")
game.computer.flop()
while True:
	ans = input("Would you like to bet or check? Type B for bet or C for check: ")
	if ans.lower() not in ('b', 'c'): print("Invalid input. Please enter B for bet or C for check: ")
	else: break
if ans.lower() == 'b':
	amount = game.player.betPrompt()
	game.player.bet(amount)
	print("Player bet placed.")
	computer_status = game.computer.computerChoice(amount)
	if computer_status > 0:
		result = game.player.callOrFold(computer_status)
		if result == 0:
			print("****THE RIVER****\n" + "Your hand: ")
			game.player.flop()
			game.player.river()
			print("Computer's hand: ")
			game.computer.flop()
			game.computer.river()
		else: print("Game over.")
	else:
		print("****THE RIVER****\n" + "Your hand: ")
		game.player.flop()
		game.player.river()
		print("Computer's hand: ")
		game.computer.flop()
		game.computer.river()
else:
	amount = 0
	computer_status = game.computer.computerChoice(amount)
	if computer_status != 0:
		result = game.player.callOrFold(computer_status) 
		if result == 0:
			print("****THE RIVER****\n" + "Your hand: ")
			game.player.flop()
			game.player.river()
			print("Computer's hand: ")
			game.computer.flop()
			game.computer.river()
		else: print("Game Over")
	else:
		print("****THE RIVER****\n" + "Your hand: ")
		game.player.flop()
		game.player.river()
		print("Computer's hand: ")
		game.computer.flop()
		game.computer.river()

# print("Player Bank: " + str(game.player.bank_balance))
# print("Pot: " + str(game.pot))
