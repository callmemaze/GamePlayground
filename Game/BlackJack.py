# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
message=""
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
     
    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0] + 1, pos[1] + CARD_BACK_CENTER[1] + 1], CARD_BACK_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.cards=[]

    def __str__(self):
        handCards = ""
        for card in self.cards:
            handCards = handCards + str(card) + " "
        if len(handCards) == 0:
            return "Hand contains nothing."
        else:
            return "Hand contains " + handCards.strip() + "."


    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        current = 0
        isAce= False
        for card in self.cards:
            rank = card.get_rank()
            current += VALUES[rank]
            if rank == "A":
                isAce = True
        if isAce and current < 12:
            current += 10
        return current
   
    def draw(self, canvas, pos):
        for card in self.cards:
            pos[0] = pos[0] + CARD_SIZE[0] + 30
            card.draw(canvas, pos) 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards=[]
        for i in SUITS:
            for j in RANKS:
                self.cards.append(Card(i,j))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        deckCards = ""
        for card in self.cards:
            deckCards = deckCards + str(card) + " "
        if len(deckCards) == 0:
            return "Deck contains nothing."
        else:
            return "Deck contains " + deckCards.strip() + "."



#define event handlers for buttons
def deal():
    global outcome, in_play,deck,player,dealer,score,message
    if in_play:
        in_play=False
        score -= 1
        deal()
    else:
        player = Hand()
        dealer = Hand()
        deck = Deck()
        deck.shuffle()
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        outcome = "Hit or Stand ? "
        message = ""
        in_play = True
    # your code goes here
    
    

def hit():
    global player,message,in_play,outcome,score
    if in_play:
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())
            if player.get_value() > 21:
                message = "You Have Busted!!"
                score -= 1
                outcome =  " New Deal ? "
                in_play = False
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play,player,dealer,score,message,outcome
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            message = "Dealer Busted !!"
            score += 1
        elif player.get_value() > dealer.get_value():
            message = "You Win"
            score += 1
        else:
            message = "You Lose"
            score -= 1
        outcome = "New Deal ??"
        in_play = False
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BLACKJACK",[150,60],50,"Aqua")
    canvas.draw_text("DEALER",[36,180],25,"Aqua")
    canvas.draw_text("PLAYER",[36,380],25,"Aqua")
    canvas.draw_text(outcome, (235, 385), 25, "White")
    canvas.draw_text(message, (235, 185), 25, "White")
    canvas.draw_text("Score:" + str(score), (450, 115), 30, "White")
    dealer.draw(canvas,[-65,200])
    player.draw(canvas,[-65,400])
    if in_play:
        dealer.cards[0].draw_back(canvas,[36,199])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Orange")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
