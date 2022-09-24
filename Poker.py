import pydealer
import random

class Game:
    def __init__(self):
        self.deck = pydealer.Deck()
        self.player = Entity(self.deck, "Player")
        self.computer = Entity(self.deck, "Computer")
        self.pot = 0
    
    def shuffle(self):
        self.deck.shuffle()

    def increasePot(self, amount):
        self.pot = self.pot + amount

class Entity:
    def __init__(self, deck, name):
        self.deck = deck
        self.bank_balance = 200
        self.hand = pydealer.Stack()
        self.name = name

    def bet(self, amount):
        self.bank_balance = self.bank_balance - amount

    def dealCards(self):
        self.hand += self.deck.deal(3)
        # print(self.hand[0])
        # print(self.hand[1])
        # print(self.hand[2])
    
    def betPrompt(self):
        amount = input("Bank Balance: $" + str(self.bank_balance) + " How much would you like to bet?: ")
        value = int(amount)
        while value > self.bank_balance or value < 5:
            amount = input("Invalid amount. Please enter a number less than your balance and more than 5. Bank Balance: $" + str(self.bank_balance) + ". ")
            value = int(amount)
        return value

    def bet(self, amount):
        if self.name == "Player":
            self.bank_balance -= amount    
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
            if game.player.bank_balance < 25:
                bet_raise = game.player.bank_balance
            else:
                bet_raise = 25
            game.computer.bet(amount + bet_raise)
            print("Computer raises $" + str(bet_raise) + ". Pot: $" + str(game.pot))
            return bet_raise

    def checkOrBet(self, amount):
        check = 0
        random_number = random.randint(1, 10)
        if random_number < 6:
            if game.player.bank_balance < 25:
                bet = game.player.bank_balance
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
            if ans.lower() not in ('c', 'f'):
                print("Invalid input. Please enter C for call or F for fold: ")
            else:
                break
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

    def river(self):
        self.showCard(2)
    
    def showSuit(self, suit):
        if suit == "Hearts":
            return "\u2665"
        elif suit == "Diamonds":
            return "\u2666"
        elif suit == "Spades":
            return "\u2660"
        elif suit == "Clubs":
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
amount = game.player.betPrompt()
game.player.bet(amount)
print("Player bet placed.")
game.computer.bet(amount)
print("Computer calls. Pot: $" + str(game.pot))
game.player.dealCards()
game.computer.dealCards()
print("****THE FLOP****\n" + 
        "Your hand: ")
game.player.flop()
print("Computer's hand: ")
game.computer.flop()
while True:
    ans = input("Would you like to bet or check? Type B for bet or C for check: ")
    if ans.lower() not in ('b', 'c'):
        print("Invalid input. Please enter B for bet or C for check: ")
    else:
        break
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
        else:
            print("Game over.")
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
        else:
            print("Game Over")  
    else:
        print("****THE RIVER****\n" + "Your hand: ")
        game.player.flop()
        game.player.river()
        print("Computer's hand: ")
        game.computer.flop()
        game.computer.river()       








# print("Player Bank: " + str(game.player.bank_balance))
# print("Pot: " + str(game.pot))
        