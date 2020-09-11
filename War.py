#####################################
### GAME OF WAR #####
#####################################


from random import shuffle
from time import sleep

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    
    def __init__(self):
        self.allcards = [(x,y) for x in RANKS for y in SUITE]

    def split_deck(self):
        '''Splits the deck in half'''
        return (self.allcards[:26], self.allcards[26:])

    def shuffle(self):
        '''Shuffles the Deck of Cards'''
        shuffle(self.allcards)




class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        '''Displays the number of cards in their hand'''
        if len(self.cards) == 1:
            return "The hand contains {} card".format(len(self.cards))
        elif len(self.cards) > 1:
            return "The hand contains {} cards".format(len(self.cards))
        return "You have no cards in your hand"

    def remove_card(self):
        '''removes a card from the hand'''
        return self.cards.pop(0)
    
    def add_cards(self, added_cards):
        '''Adds cards to the hand'''
        self.cards.extend(added_cards)






class Player:
    """
    This is the Player class, which takes in a name of the player, and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def play_card(self):
        '''Use the remove_card() method from the class Hand to play a card called drawn_card. 
        Print what card was played. Then return the drawn_card'''
        drawn_card = self.hand.remove_card()
        print("{} has played the {} of {}".format(self.name, drawn_card[0], drawn_card[1]))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        ''' Removes three cards from the beginning of the deck (index 0) and adds them
            to a list called war_cards. If there are less than 3 cards in the hand,
            Do not add any cards to war_cards. Finally, Returns the list called war_cards'''
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for i in range(3):
                war_cards.append(self.hand.cards.pop(0))
            return war_cards
    
    def still_has_cards(self):
        '''Return True if still has cards in hand'''
        return len(self.hand.cards) != 0
        
        


######################
#### GAME PLAY #######
######################

print("\nWelcome to War, let's begin...")
print("\n")

game_deck = Deck()
game_deck.shuffle()
player1_deck, player2_deck = game_deck.split_deck()
player1_hand = Hand(player1_deck)
player2_hand = Hand(player2_deck)




player1 = Player(input("Please enter the name of Player 1: "), player1_hand)
player2 = Player(input("Please enter the name of Player 2: "), player2_hand)
print("\n")

print("Welcome {} and {}! Player 1 will go first".format(player1.name, player2.name))
print('---------------------------------------------------------------')
# sleep(1)

while player1.still_has_cards() and player2.still_has_cards():
    p1_card = player1.play_card()
    # sleep(1)
    p2_card = player2.play_card()
    # sleep(1)

    if p1_card[0] == p2_card[0]:
        war_pile = []
        war_pile.append(p1_card)
        war_pile.append(p2_card)
        print('\n')
        print("WAR!!")
        print('\n')
        print('\n')
        # sleep(2)
        war_pile.extend(player1.remove_war_cards())
        war_pile.extend(player2.remove_war_cards())
        if len(player1.hand.cards) >= 1 and len(player2.hand.cards) >= 1:
            p1_card_war = player1.play_card()
            print('\n')
            p2_card_war = player2.play_card()
            war_pile.append(p1_card_war)
            war_pile.append(p2_card_war)
        # sleep(0.5)
        while p1_card_war[0] == p2_card_war[0] :
            p1_card_war = player1.play_card()
            print('\n')
            p2_card_war = player2.play_card()
            war_pile.append(p1_card_war)
            war_pile.append(p2_card_war)
        
        if RANKS.index(p1_card_war[0]) > RANKS.index(p2_card_war[0]):
            print("{} wins!".format(player1.name))
            player1.hand.add_cards(war_pile)
        elif RANKS.index(p1_card_war[0]) < RANKS.index(p2_card_war[0]):
            print("{} wins!".format(player2.name))
            player2.hand.add_cards(war_pile)
        else:
            print("THERE IS AN ERROR IN THE WAR LOOP")

    elif RANKS.index(p1_card[0]) > RANKS.index(p2_card[0]):
        print("{} wins!".format(player1.name))
        player1.hand.add_cards([p2_card, p1_card])
    elif RANKS.index(p1_card[0]) < RANKS.index(p2_card[0]):
        print("{} wins!".format(player2.name))
        player2.hand.add_cards([p1_card, p2_card])
    else:
        print("THERE IS AN ERROR IN THE MAIN GAME LOOP")
    # sleep(0.5)
    print('\n')
    print("########################################")
    print('\n')
    print("{}'s hand:".format(player1.name))
    print(player1.hand)
    print('\n')
    print("{}'s hand:".format(player2.name))
    print(player2.hand)
    print("########################################")
    print('\n')
    input("Press Enter to play the next round.")
    print('\n')
    print('\n')
    # sleep(2)
    print(player1.still_has_cards(), player2.still_has_cards())
        
        




