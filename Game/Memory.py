# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def new_game():
    global deck, exposed, state, index1, index2, score, moves
    state, score, moves, index1, index2 = 0, 0, 0, -1, -1
    lst1=[0,1,2,3,4,5,6,7]
    lst2=[0,1,2,3,4,5,6,7]
    deck=lst1+lst2
    random.shuffle(deck)
    exposed=[False]*16
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state,index1,index2,score,moves
    cardIndex=list(pos)[0]//50
    if not exposed[cardIndex]:
        if state==0:
            index1=cardIndex
            exposed[cardIndex]=True
            state=1
        elif state==1:
            index2=cardIndex
            exposed[cardIndex]=True
            if deck[index1]==deck[index2]:
                score+=1
            state=2 
            moves+=1
            label.set_text("Turns = 0"+str(moves))
        else:
            if deck[index1]!=deck[index2]:
                exposed[index1],exposed[index2]=False,False
                index1= -1
                index2= -1
            index1 = cardIndex
            exposed[cardIndex] = True
            state = 1
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck
    for i in range(len(deck)):
        if exposed[i]:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "Red", "Black")
            canvas.draw_text(str(deck[i]), (i*50+20, 59), 25, "White")
        else:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "Red", "Blue") 
    label.set_text("Turns = " + str(moves))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
