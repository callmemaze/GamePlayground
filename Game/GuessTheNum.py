#GUESS THE NUMBER

# helper function to start and restart the game
import simplegui
import random

secretNumber = 0
range=100
guesses=0
def new_game():
    # initialize global variables used in your code here
    global secretNumber
    global range
    global guesses
    secretNumber=random.randrange(0,range)
    if range==100:
        guesses=7
    elif range==1000:
        guesses=10
    print("New game. Range is [0,100)")
    print("Number of remaining guesses is",guesses)
    pass


#event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range=100
    new_game()   
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    range=1000
    new_game()
    pass
    
def input_guess(guess):
    # main game logic
    global secretNumber
    global guesses
    guess=int(guess)
    print("Guess was",guess)
    guesses=guesses-1
    print("Number of remaining guesses is",guesses)
    if guess==secretNumber:
        print("Correct!")
    elif guess<secretNumber:
        print("Higher")
    elif guess>secretNumber:
        print("Lower")
    
    if guess==secretNumber:
        print("You Won!")
        new_game()
    if guesses==0:
        print("Out of guess!")
        new_game()
    else:
        pass
    pass

    
# create frame
frame=simplegui.create_frame("Guess The Number",200,200)


# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)",range100,150)
frame.add_button("Range is [0,1000)",range1000,150)
input_guess=frame.add_input("Enter your Guess",input_guess,150)

# call new_game 
new_game()
frame.start()
