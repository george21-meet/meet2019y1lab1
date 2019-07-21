import turtle
t=turtle.Turtle()
i=0

# Everything that comes after the # is a 
# comment.
# It is a note to the person reading the code.
# The computer ignores it.
# Write your code below here...
t.penup() #Pick up the pen so it doesn’t 
               #draw
t.goto(-200,-100) #Move the turtle to the 
 #position (-200, -100) 
 #on the screen
t.pendown() #Put the pen down to start
                 #drawing
t.goto(-200,100) 
t.goto(-200+50,-100) 
t.goto(-200+100,-100+200)
t.goto(-200+100,-100)
for p in range(2):
    t.penup()
    t.goto(i,100)
    t.pendown()
    t.fd(100)
    t.back(100)
    t.right(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.back(100)
    t.right(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    i+=150
t.penup()
t.goto(300,100)
t.pendown()
t.fd(100)
t.back(50)
t.right(90)
t.fd(200)
