import turtle
import random
import time
delay=0.1
score=0
high_score=0

#Creating Screen.
sc=turtle.Screen()
sc.bgcolor("cyan")
sc.bgpic("20220323_162053_0000.png")
sc.title("Snake game by Tannu")
sc.tracer(0)

#Creating Head.
h=turtle.Turtle()
h.speed()
h.shape("square")
h.color("black")
h.shapesize(3,3)
h.penup()
h.goto(0,200)
h.direction="stop"
segment = []


#Creating Food
f=turtle.Turtle()
f.speed(0)
f.shape("circle")
f.color("red")
f.penup()
f.shapesize(2,2)
f.goto(0,0)

#Scores
sr=turtle.Turtle()
sr.speed(0)
sr.shape("square")
sr.color("Black")
sr.penup()
sr.hideturtle()
sr.goto(0,965)
sr.write("Score:0 High Score:0",align="center",font=("Courier", 10, "normal"))

#Functions.	
def go_up():
		h.direction="Up"
def go_down():
		h.direction="Down"
def go_right():
		h.direction="Right"
def go_left():
		h.direction="Left"
def move():
    if h.direction == "Up":
        y = h.ycor()
        h.sety(y+20)
    if h.direction == "Down":
        y = h.ycor()
        h.sety(y-20)
    if h.direction == "Left":
        x = h.xcor()
        h.setx(x-20)
    if h.direction == "Right":
        x = h.xcor()
        h.setx(x+20)
sc.listen()
sc.onkeypress(go_up,"Up")
sc.onkeypress(go_down,"Down")
sc.onkeypress(go_right,"Right")
sc.onkeypress(go_left,"Left")
while True:
	   sc.update()
	   if h.xcor()>440 or h.xcor()<-440 or h.ycor()>860 or h.ycor()<-860:
	   	time.sleep(0.3)
	   	h.goto(0,0)
	   	h.direction="stop"
	   if h.distance(f)<30:
	   	x=random.randint(-200,300)
	   	y=random.randint(-200,300)
	   	f.goto(x,y)
	   	new_segment = turtle.Turtle()
	   	new_segment.speed(0)
	   	new_segment.shape("square")
	   	new_segment.shapesize(3,3)
	   	new_segment.color("black")
	   	new_segment.penup()
	   	segment.append(new_segment)
	   	delay -=0.001
	   	score+=10
	   	if score>high_score:
	   		high_score=score
	   		sr.clear()
	   		sr.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("Courier", 10, "normal"))
	   for body in range(len(segment)-1,0,-1):
	   	x=segment[body-1].xcor()
	   	y=segment[body-1].ycor()
	   	segment[body].goto(x,y)
	   	
	   if len(segment)>0:
	    	x=h.xcor()
	    	y=h.ycor()
	    	segment[0].goto(x,y)
	    
	   move()
	   for segments in segment:
	           if segments.distance(h)<20:
	           	time.sleep(1)
	           	h.goto(0, 0)
	           	h.direction = "stop"
	           	colors = random.choice(['red', 'blue', 'green'])
	           	shapes = random.choice(['square', 'circle'])
	           	for segments in segment:
	           		segments.goto(900,900)
	           	segment.clear()
	           	score = 0
	           	delay = 0.1
	           	sr.clear()
	           	sr.write("Score : {} High Score{}".format(score, high_score),align="center",font=("Courier",10, "normal"))
	   time.sleep(0.1)
