import turtle
t=turtle.Turtle()
i=50

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
t.penup()
t.goto(50,100)
t.pendown()
t.goto(100,100)
t.goto(-25,100)
t.goto(-25,0)
t.goto(100,0)
t.penup()
t.goto(-25,0)
t.pendown()
t.goto(-25,-100)
t.goto(100,-100)

t.penup()
t.goto(100,100)
t.pendown()
t.goto(150,200)
t.goto(0,200)
t.goto(0,100)
t.goto(150,100)
t.penup()
t.goto(0,100)
t.pendown()
t.goto(0,0)
t.goto(150,0)




# ...and end it before the next line.
turtle.mainloop() 
# turtle.mainloop() tells the turtle to do all
# the turtle commands above it and paint it on the screen.
# It always has to be the last line of code!
