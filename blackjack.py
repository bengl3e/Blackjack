from random import shuffle
class deck:
    #This class creates a deck from numbers. 1-A 2-10 and 11-13 being J Q K Respectively.
    #This class has one Field and 3 Methods
    #
    #Fields
    #cards:List of Cards 
    #
    #Methods
    #Constructor
    #show():Shows the current deck in use.
    #hit(): Will return one value and also replace the deck if emptied
    def __init__(self):
        self.cards = list(range(1,14))
        self.cards = self.cards+ self.cards
        self.cards = self.cards+ self.cards
        shuffle(self.cards)
    def show(self):
        return self.cards
    def hit(self):
        if len(self.cards) ==0:
            self.cards = list(range(1,14))
            self.cards = self.cards+ self.cards
            self.cards = self.cards+ self.cards
            shuffle(self.cards)
        return self.cards.pop()

class player:
    #this is a player class which has a 5 fields and 3 Method to keep track of players.
    #Score = Current Card Score.
    #Money = amount of currency available. Default is 10
    #Bust = Flag for if a player bust or not.
    #End = Player has quit playing either out of lack of funds or reached goal.
    #Cards = List of current Hand.
    #
    #It has 3 Methods:
    #Constructer
    #setM:Called to Set Money if necessary
    #clear:Clear hand/score for next round.
    def __init__(self):
        self.score = 0
        self.money = 10
        self.stop = False
        self.bust = False
        self.end = False
        self.cards = []
        
    def setM(self, cash):
        self.money = cash
        
    def hit(self,card):
        if card==11:
            self.cards.append('J')
        elif card == 12:
            self.cards.append('Q')
        elif card == 13:
            self.cards.append('K')
        elif card == 1:
            self.cards.append('A')
        else:
            self.cards.append(card)
        if card>10:
            card = 10
        if card ==1:
            if self.score + 11 <21:
                self.score = self.score +11
            else:
                self.score = self.score +1
        else:
            self.score = self.score + card

        #Here Is where the simple Strategy comes in.
        if self.score >16:
            self.stop = True
        if self.score>21:
            self.bust = True

    def clear(self):
        self.score =0
        self.cards =[]
        self.stop =False
        self.bust = False


class blackjack:
    #This is the Class in which the game is played. It has 4 Fields and 6 Methods to simulate the game.
    #
    #The Class has 4 Fields,
    #deck:The current deck in use.
    #p1:Player 1
    #p2:Player 2
    #p1t:Player 1 Target money Value
    #p2t: Player 2 Target Money Value
    #Dealer: Dealer or House
    #
    #Methods
    #Constructor
    #m: Show Players Currency(for debug purposes)
    #show(): Used to print the result to the console.
    #setup(): Sets up a new hand in which everyone who wants to play starts out with two cards.
    #round(): Simulates one round of blackjack.
    #run(): Runs the entire simulation.
    
    def __init__(self):
        self.deck = deck()
        self.p1 = player()
        self.p2 = player()
        self.dealer = player()
        self.p1t = 15
        self.p2t = 15

    def m(self):
        print(self.p1.money)
        print(self.p2.money)
    
    def show(self):
        print ("--------------------------------------")
        if self.p1.end ==False:
            print("Player 1: Cards:",self.p1.cards, "Score:", self.p1.score)
        else:
            print("P1 has Completed")
        if self.p2.end==False:
            print("Player 2: Cards:",self.p2.cards, "Score:", self.p2.score)
        else:
            print("P2 has Compelted")
        print("Player Dealer: Cards:",self.dealer.cards, "Score:", self.dealer.score)
        self.m()
        
    def setup(self):
        self.dealer.clear()
        if (self.p1.money < 1):
            self.p1.end =True
        if (self.p2.money <1):
            self.p2.end = True
        if self.p1.end ==False:
            self.p1.clear()
            self.p1.money = self.p1.money-1
            self.p1.hit(self.deck.hit())
            self.p1.hit(self.deck.hit())
        if self.p2.end ==False:
            self.p2.clear()
            self.p2.money = self.p2.money-1
            self.p2.hit(self.deck.hit())
            self.p2.hit(self.deck.hit())
        self.dealer.hit(self.deck.hit())
        self.dealer.hit(self.deck.hit())

        
    def round(self):
        self.setup()
        print("----------------------------------")
        round = False
        while(round ==False):
            if (self.p1.stop == False):
                self.p1.hit(self.deck.hit())
            if (self.p2.stop == False):
                self.p2.hit(self.deck.hit())
            if (self.dealer.stop == False):
                self.dealer.hit(self.deck.hit())
            if (self.p1.stop ==True and self.p2.stop == True and self.dealer.stop == True):
                if (self.p1.bust ==False and self.p1.end ==False):
                    if (self.dealer.bust ==True):
                        print("p1 Win")
                        self.p1.money = self.p1.money +2
                        if self.p1.money >self.p1t-1:
                            self.p1.end =True
                    elif (self.p1.score >self.dealer.score):
                            print("p1 Win")
                            self.p1.money = self.p1.money +2
                            if self.p1.money >self.p1t-1:
                                self.p1.end =True
                    elif (self.p1.score == self.dealer.score):
                        print("p1 Tied")
                        self.p1.money = self.p1.money +1
                    else:
                        print("p1 Loss ")
                else:
                     if self.p1.money == 0:
                         self.p1.end = True
                     elif self.p1.end ==True:
                        print("p1 has finished")
                     else:
                         print("p1 Loss")
                if(self.p2.bust ==False and self.p2.end ==False):
                    if (self.dealer.bust ==True):
                        print("p2 Win")
                        self.p2.money = self.p2.money +2
                        if self.p2.money >self.p2t-1:
                            self.p2.end =True
                    elif (self.p2.score >self.dealer.score):
                            print("p2 Win")
                            self.p2.money = self.p2.money +2
                            if self.p2.money >self.p2t-1:
                                self.p2.end =True
                    elif (self.p2.score == self.dealer.score):
                        print("p2 Tied")
                        self.p2.money = self.p2.money +1
                    else:
                        print("p2 Loss")
                else:
                    if self.p2.money ==0:
                        self.p2.end =True
                    elif self.p2.end ==True:
                        print("p2 has finished")
                    else:
                        print ("p2 Loss")
                round =True
        self.show()


    def run(self):
        x = True
        while (x==True):
            if (self.p1.end ==True and self.p2.end ==True):
                x = False
            else:
                self.round()
