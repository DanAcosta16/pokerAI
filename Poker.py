import pydealer

class Game:
    def __init__(self):
        self.deck = pydealer.Deck()
        self.player = Entity(self.deck)
        self.computer = Entity(self.deck)
        self.pot = 0
    
    def shuffle(self):
        self.deck.shuffle()

    def increasePot(self, amount):
        self.pot = self.pot + amount

class Entity:
    def __init__(self, deck):
        self.deck = deck
        self.bank_balance = 1000
        self.hand = pydealer.Stack()

    def bet(self, amount):
        self.bank_balance = self.bank_balance - amount

    def dealCards(self):
        self.hand += self.deck.deal(3)
        print(self.hand[0])
        print(self.hand[1])
        print(self.hand[2])



game = Game()
game.shuffle()
amount = input("Bank Balance: " + str(game.player.bank_balance) + " How much would you like to bet?: ")
value = int(amount)
while value > game.player.bank_balance or value < 100:
    amount = input("Invalid amount. Please enter a number less than your balance and more than 100. Bank Balance: " + str(game.player.bank_balance) + " ")
    value = int(amount)
game.player.bet(value)
game.increasePot(value)
print("Bet placed.")
game.player.dealCards()
game.computer.dealCards()
# print("Player Bank: " + str(game.player.bank_balance))
# print("Pot: " + str(game.pot))
        