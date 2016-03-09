from blackjack import *
import unittest

class BlackjackTest(unittest.TestCase):
    def setUp(self):
        self.tdeck1 = deck()
        self.tdeck2 = deck()
        self.tbj = blackjack()
        self.tplayer = player()
        
    def test_contains_deck(self):
        print()
        print("Testing Hit method of refreshing deck")
        print(len(self.tdeck1.cards))
        for i in range(0,52):
            self.tdeck1.cards.pop()
        print(len(self.tdeck1.cards))
        self.tdeck1.hit()
        self.assertEqual(len(self.tdeck1.cards), 51)
        print("Testing Method Show()")
        self.assertEqual(self.tdeck1.show(), self.tdeck1.cards)

    def test_contains_player(self):
        print()
        print("Testing New Player SetM by setting Money to 25")
        print("Current Money",self.tplayer.money)
        self.tplayer.setM(25);
        print("New Money", self.tplayer.money)
        self.assertEqual(self.tplayer.money,25)
        print("Try Hitting Empty Hand")
        print("Current hand:",self.tplayer.cards, "Adding:", 10)
        self.tplayer.hit(10)
        print("New Hander:", self.tplayer.cards)
        self.assertEqual(self.tplayer.cards[0],10)
        print("Hitting Again, Adding",7)
        self.tplayer.hit(7)
        self.assertEqual(self.tplayer.cards[1],7)
        self.tplayer.hit(11)
        print("Adding 11, should change to J and cause error as J!=11")
        self.assertNotEqual(self.tplayer.cards[2],11)
        print("current Cards",self.tplayer.cards, "checking score should be 27")
        self.assertEqual(self.tplayer.score,27)
        print("current score:",self.tplayer.score)
        self.tplayer.clear()
        print("Testing Clear Cards:",self.tplayer.cards,"Score:",self.tplayer.score)
        self.assertEqual(self.tplayer.cards,[])
        self.assertEqual(self.tplayer.score,0)



    def test_contains_blackjack(self):
        self.tbj.run()
        
    

if __name__ == '__main__':
        unittest.main(verbosity=3)
        
