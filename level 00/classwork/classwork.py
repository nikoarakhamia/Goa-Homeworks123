

from os import read
from turtle import *

speed(2) 
width(7)
color("red")
begin_fill()
forward(200) 
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

forward(70)
color("brown") 
begin_fill()
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90)
end_fill()

penup()
goto(200, 200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("purple")
penup()
begin_fill()
goto(25, 110)
right(150)
pendown()
forward(60)
right(90)
forward(50)
right(90)
forward(60)
right(90)
forward(50)
end_fill()

color("purple")
penup()
goto(175,110)
begin_fill()
pendown()
forward(50)
right(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)
end_fill()


exitonclick()