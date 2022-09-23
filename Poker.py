import pydealer

class Game:
    def __init__(self):
        self.deck = pydealer.Deck()
        self.player = Entity(self.deck, "player")
        self.computer = Entity(self.deck, "computer")
        self.pot = 0
    
    def shuffle(self):
        self.deck.shuffle()

    def increasePot(self, amount):
        self.pot = self.pot + amount

class Entity:
    def __init__(self, deck, name):
        self.deck = deck
        self.bank_balance = 1000
        self.hand = pydealer.Stack()
        self.name = name

    def bet(self, amount):
        self.bank_balance = self.bank_balance - amount

    def dealCards(self):
        self.hand += self.deck.deal(3)
        # print(self.hand[0])
        # print(self.hand[1])
        # print(self.hand[2])

    def bet(self):
        amount = input("Bank Balance: " + str(self.bank_balance) + " How much would you like to bet?: ")
        value = int(amount)
        while value > self.bank_balance or value < 100:
            amount = input("Invalid amount. Please enter a number less than your balance and more than 100. Bank Balance: " + str(self.bank_balance) + ". ")
            value = int(amount)
        self.bank_balance = self.bank_balance - value
        return value

    def flop(self):
        print("****THE FLOP****\n" + 
        "Your hand: ")
        self.showCard(0)
        self.showCard(1)
    
    def showSuit(self, suit):
        match suit:
            case "Hearts":
                return "\u2665"
            case "Diamonds":
                return "\u2666"
            case "Spades":
                return "\u2660"
            case "Clubs":
                return "\u2663"


    def showCard(self, index):
        print(self.hand[index].value + " " + self.showSuit(self.hand[index].suit))
        
            


    




game = Game()
game.shuffle()

# amount = input("Bank Balance: " + str(game.player.bank_balance) + " How much would you like to bet?: ")
# value = int(amount)
# while value > game.player.bank_balance or value < 100:
#     amount = input("Invalid amount. Please enter a number less than your balance and more than 100. Bank Balance: " + str(game.player.bank_balance) + " ")
#     value = int(amount)
bet = game.player.bet()
game.increasePot(bet)
print("Bet placed.")
game.player.dealCards()
game.computer.dealCards()
game.player.flop()
ans = input("Would you like to bet or check? Type B for bet or C for check: ")
if ans == 'b' or ans == 'B':
    bet = game.player.bet()
    game.increasePot(bet)
    print("Bet placed.")




# print("Player Bank: " + str(game.player.bank_balance))
# print("Pot: " + str(game.pot))
        