# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 15
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel=[0,0]
paddle1_pos, paddle2_pos = (HEIGHT - PAD_HEIGHT)/2, (HEIGHT - PAD_HEIGHT)/2
paddle1_vel=0
paddle2_vel=0
score1=0
score2=0
started=False
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("https://i.imgur.com/npmQ5Rb.png")
#ball_vel=[0,0]
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel[0]= random.randrange(120, 240) / 60
        ball_vel[1]= -random.randrange(60,180) / 60
    if direction == LEFT:
        ball_vel[0]= -random.randrange(120, 240) / 60
        ball_vel[1]= -random.randrange(60,180) / 60
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.choice([RIGHT,LEFT]))
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,started
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]  
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "white","White")
 
    # update paddle's vertical position, keep paddle on the screen
    if 0 <= (paddle1_pos + paddle1_vel) <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if 0 <= (paddle2_pos + paddle2_vel) <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    # draw paddles
    canvas.draw_line([PAD_WIDTH / 2, paddle1_pos],[PAD_WIDTH / 2, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH-PAD_WIDTH / 2, paddle2_pos],[WIDTH-PAD_WIDTH / 2, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "White")
    # determine whether paddle and ball collide    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1] 
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1]= -ball_vel[1]
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH :
        if paddle1_pos <= ball_pos[1] <= (paddle1_pos + PAD_HEIGHT):
            sound=simplegui.load_sound('https://freesound.org/people/NoiseCollector/sounds/4391/download/4391__noisecollector__pongblipf-5.wav')
            sound.play()
            ball_vel[0]= - 1.1 * ball_vel[0] 
        else:
            spawn_ball(RIGHT)
            score2+=1
            sound=simplegui.load_sound('https://freesound.org/people/leviclaassen/sounds/107789/download/107789__leviclaassen__hit-002.wav')
            sound.play()
    if ball_pos[0] >= WIDTH -BALL_RADIUS - PAD_WIDTH : 
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos + PAD_HEIGHT):
            sound=simplegui.load_sound('https://freesound.org/people/NoiseCollector/sounds/4391/download/4391__noisecollector__pongblipf-5.wav')
            sound.play()
            ball_vel[0]= - 1.1 * ball_vel[0] 
        else:
            spawn_ball(LEFT)
            score1+=1
            sound=simplegui.load_sound('https://freesound.org/people/leviclaassen/sounds/107789/download/107789__leviclaassen__hit-002.wav')
            sound.play()
    #if score1==2:
        #message="Player1 Wins!"
        #canvas.draw_text(message,(100,200),30,"White")
        
    #elif score2==5:
        #message="Player2 Wins!"
        #canvas.draw_text(message,(400,200),30,"White") 
        
        
    # draw scores
    canvas.draw_text(str(score1),(200,20),20,"White") 
    canvas.draw_text(str(score2),(400,20),20,"White") 
    
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
def keydown(key):
    acc=5
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = -acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = acc 
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = acc
    elif key==simplegui.KEY_MAP["up"]:  
        paddle2_vel = -acc
    
def keyup(key):
    acc=1
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0 
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["up"]:  
        paddle2_vel = 0

def click(pos):
    global started,Max_rock,score,lives
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        new_game()
        
def restart():
    global score1,score2,started,ball_vel,ball_pos
    new_game()
    score1=0
    score2=0
    ball_vel=[0,0]
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    started=False
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)
frame.add_button("Restart", restart, 100)

# start frame

frame.start()
