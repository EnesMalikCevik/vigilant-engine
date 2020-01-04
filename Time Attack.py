#Python Turtle Game
import turtle
import math
import random
import os
import time

  

#Setting up screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.bgpic("background.png")
screen.title("Time Attack - A Python Turtle Game")

#Drawing borders
mypen = turtle.Turtle()
mypen.color("darkviolet")
mypen.penup()
mypen.setposition(-325,-325)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(650)
    mypen.left(90)
mypen.hideturtle()


#Creating the health variable and printing it
health = 3
mypen.penup()
mypen.setposition(248, 329)
healthstring = "Health: %s" %health
mypen.write(healthstring, True, align="left", font=("Arial",14, "normal"))
   



#Creating player
player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(random.randint(-300, 300), random.randint(-300, 300))
player.shapesize(0.7,1)




#Creating the score variable
score = 0


#Setting speed variable
speed = 15

#Creating goals
minus_scores = 5
plus_scores = 5
health_ = 2

plus_goals = []
minus_goals = []
health_goals = []

for i in range(plus_scores):
    plus_goals.append(turtle.Turtle())
    plus_goals[i].color("green")
    plus_goals[i].shape("circle")
    plus_goals[i].penup()
    plus_goals[i].speed(15)
    
    plus_goals[i].setposition(random.randint(-300, 300), random.randint(-300, 300))

for i in range(minus_scores):
    minus_goals.append(turtle.Turtle())
    minus_goals[i].color("gold")
    minus_goals[i].shape("circle")
    minus_goals[i].penup()
    minus_goals[i].speed(0)
    minus_goals[i].setposition(random.randint(-300, 300), random.randint(-300, 300))

for i in range(health_):
    health_goals.append(turtle.Turtle())
    health_goals[i].color("red")
    health_goals[i].shape("circle")
    health_goals[i].penup()
    health_goals[i].speed(0)
    health_goals[i].setposition(random.randint(-300, 300), random.randint(-300, 300))


#plus 2 points
plus_two = turtle.Turtle()
plus_two.color("pink")
plus_two.shape("circle")
plus_two.penup()
plus_two.speed(0)
plus_two.setposition(random.randint(-300, 300), random.randint(-300, 300))




#Speed enhancer
speed_up = turtle.Turtle()
speed_up.color("black")
speed_up.shape("circle")
speed_up.penup()
speed_up.speed(0)
speed_up.setposition(random.randint(-300, 300), random.randint(-300, 300))


#Speed reducer
speed_down = turtle.Turtle()
speed_down.color("black")
speed_down.shape("circle")
speed_down.penup()
speed_down.speed(0)
speed_down.setposition(random.randint(-300, 300), random.randint(-300, 300))





#Define functions
def turnleft():
    player.left(30)
    
def turnright():
    player.right(30)
    

    
def CollisionDetector(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 22:
        return True
    else:
        return False
        
#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnleft, "A")
turtle.onkey(turnleft, "a")
turtle.onkey(turnright, "Right")
turtle.onkey(turnright, "D")
turtle.onkey(turnright, "d")



#starting time so that the program can calculate the total time spent
start_time = time.time()




while score<20:
    
    player.forward(speed)
    
    #Boundary checking for player
    if player.xcor() > 325 or player.xcor() < -325:
        player.right(180)
        os.system("afplay bounce.mp3&") 
   
    if player.ycor() > 325 or player.ycor() < -325:
        player.right(180)
        os.system("afplay bounce.mp3&") 
        
    #Moving plus_goals
    for i in range(plus_scores):
        plus_goals[i].forward(speed-2)

        #Boundary Checking for plus_goals
        if plus_goals[i].xcor() > 315 or plus_goals[i].xcor() < -315:
            plus_goals[i].right(180)
            
                
       
        if plus_goals[i].ycor() > 315 or plus_goals[i].ycor() < -315:
            plus_goals[i].right(180)
                

        #Collision checking for plus_goals
        if CollisionDetector(player, plus_goals[i]):
            plus_goals[i].setposition(random.randint(-300, 300), random.randint(-300, 300))
            plus_goals[i].right(random.randint(0,360))
            os.system("afplay collision.mp3&")
            score += 1
            
            
            
            #Draw the score on the screen
            mypen.undo()
            mypen.setposition(-300, 329)
            scorestring = "Score: %s" %score
            mypen.write(scorestring, False, align="left", font=("Arial",14, "normal"))
            
            
    #Moving minus_goals
    for i in range(minus_scores):
        minus_goals[i].forward(speed-1)

        #Boundary Checking for minus_goals
        if minus_goals[i].xcor() > 315 or minus_goals[i].xcor() < -315:
            minus_goals[i].right(180)
            
                
        #Boundary Checking for minus_goals
        if minus_goals[i].ycor() > 315 or minus_goals[i].ycor() < -315:
            minus_goals[i].right(180)
               
 

        #Collision checking for minus_goals
        if CollisionDetector(player, minus_goals[i]):
            minus_goals[i].setposition(random.randint(-300, 300), random.randint(-300, 300))
            minus_goals[i].right(random.randint(0,360))
            os.system("afplay collision.mp3&")
            
            score -= 1
            
    
            
            #Draw the score on the screen
            mypen.undo()
            mypen.setposition(-300, 329)
            scorestring = "Score: %s" %score
            mypen.write(scorestring, False, align="left", font=("Arial",14, "normal"))
                
    #Moving health
    for i in range(health_):
        health_goals[i].forward(speed-2)

        #Boundary Checking for health
        if health_goals[i].xcor() > 315 or health_goals[i].xcor() < -315:
            health_goals[i].right(180)
            
                
        if health_goals[i].ycor() > 315 or health_goals[i].ycor() < -315:
            health_goals[i].right(180)
                
 

        #Collision checking for health
        if CollisionDetector(player, health_goals[i]):
            health_goals[i].setposition(random.randint(-300, 300), random.randint(-300, 300))
            health_goals[i].right(random.randint(0,360))
            os.system("afplay collision.mp3&")
            health -= 1
            
    
            
            #Draw the health on the screen
            mypen.undo()
            mypen.setposition(248, 329)
            healthstring = "Health: %d" %health
            mypen.write(healthstring, False, align="left", font=("Arial",14, "normal"))
    
    
    
    plus_two.forward(speed-2)
    #Boundary Checking for plus_two
    if plus_two.xcor() > 315 or plus_two.xcor() < -315:
        plus_two.right(180)
        
                
        
    if plus_two.ycor() > 315 or plus_two.ycor() < -315:
        plus_two.right(180)
         
 

    #Collision checking for plus_two
    if CollisionDetector(player, plus_two):
        plus_two.setposition(random.randint(-300, 300), random.randint(-300, 300))
        plus_two.right(random.randint(0,360))
        os.system("afplay collision.mp3&")
        score += 2
        
    
    
    
    
    
    
    speed_up.forward(speed-2)
    #Boundary Checking for speed_up
    if speed_up.xcor() > 315 or speed_up.xcor() < -315:
        speed_up.right(180)
        
                
        
    if speed_up.ycor() > 315 or speed_up.ycor() < -315:
        speed_up.right(180)
           
 

    #Collision checking for speed_up
    if CollisionDetector(player, speed_up):
        speed_up.setposition(random.randint(-300, 300), random.randint(-300, 300))
        speed_up.right(random.randint(0,360))
        os.system("afplay collision.mp3&")
        speed += 2.2
    
    
    speed_down.forward(speed-1)
    #Boundary Checking for speed_down
    if speed_down.xcor() > 315 or speed_down.xcor() < -315:
        speed_down.right(180)
        
                
        
    if speed_down.ycor() > 315 or speed_down.ycor() < -315:
        speed_down.right(180)
           
 

    #Collision checking for speed_down
    if CollisionDetector(player, speed_down):
        speed_down.setposition(random.randint(-300, 300), random.randint(-300, 300))
        speed_down.right(random.randint(0,360))
        
        speed -= 1.5
    
    if health < 1:
        os.system("afplay bye bye.mp3&")
        break
    
#Calculating last time    
last_time = time.time()
elapsed_time = last_time - start_time

#Printing the results    
mypen.setposition(-118, 100)
scorestring = "Score: %s" %score
mypen.write(scorestring, False, align="left", font=("Arial",40, "bold"))

mypen.setposition(-235, 0)
timestring = "Time: %.4s seconds" %elapsed_time
mypen.write(timestring, False, align="left", font=("Arial",40, "bold"))
            
            



