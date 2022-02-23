#######################################################
#
# COSC 140 Homework 2, "face" problem
#
#######################################################

import turtle
import random 

c = turtle.Turtle()
# I am not an artist 
#SO I WILL BE DOING ABSTRACT ART
def drawS():
  for i in range(4):
    c.forward(150)
    c.left(90)
  c.forward(150)

sc = turtle.Screen()
sc.mode('world')
c.getscreen()
sc.title("FINISH LINE OR ABSTRACT ????")
sc.setworldcoordinates(0, 0, 1100, 1100)

c.speed('fastest')

for i in range(8):
  c.up()
  c.setpos(-100, 150 * i)

  c.down()
  for j in range(8):
    if (i +j)%2==0:
      col= 'black'
    else:
      col='white'
    c.fillcolor(col)
    c.begin_fill()
    drawS()
    c.end_fill()
#c.hideturtle()
#turtle.done()



def doAnimation(radius,num,x,y):
  c.penup()
  c.setpos(x,y)
  c.pendown()  
  r= radius
  n=num
  
  for i in range(1, n):
    x,y,z= random.random(),random.random(), random.random()
    c.fillcolor(x,y,z)
    c.begin_fill()
    c.circle(r * i)
    c.end_fill()
doAnimation(20,10,500,500)
doAnimation(15,10,200,200)
doAnimation(10,10,800,800)
doAnimation(20,10,100,100)
doAnimation(20,10,100,200)
doAnimation(20,20,50,800)
#doAnimation(20,50,900,10)
#doAnimation(20,400,500,10)
#party time 
for i in range(1000):
  x= random.randrange(1,1000)
  y=random.randrange(1,1000)
  doAnimation(5,10,x,y)
 
turtle.Screen().exitonclick()


