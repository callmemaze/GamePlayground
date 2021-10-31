# template for "Stopwatch: The Game"
import simplegui
# define global variables
count=0
interval=100
stops=0
totalStop=0
stop=True


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    min = int(t / 600) % 600
    sec = int(t / 10) % 10
    tenthSec = t % 10
    tenthMin = int(t / 100) % 6
    displayMessage = str(min) + ":" + str(tenthMin) + str(sec) + "." + str(tenthSec)
    return displayMessage
pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stop,count
    stop=False
    timer.start()

def stop():
    global stops,totalStop,stop
    if stop == False:
        if count % 10 == 0 and count != 0:
            stops += 1
            totalStop+=1
        elif count!=0:
            totalStop+=1
    stop=True
    timer.stop()
    
def reset():
    global count,totalStop,stops,stop
    count = 0
    totalStops=0
    stops=0
    stop=True
    timer.stop()
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count+=1

# define draw handler
def draw(canvas):
    message=format(count)
    canvas.draw_text(message,[60,100], 36, "white")
    canvas.draw_text(str(stops)+"/"+str(totalStop),[120,30], 25,"white")
    
# create frame
frame=simplegui.create_frame("Test",200,200)
#frame.set_canvas_background('Fuchsia')
# register event handlers


frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, timer_handler)
# start frame
frame.start()
