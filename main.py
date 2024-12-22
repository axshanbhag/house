import turtle as trtl

painter = trtl.Turtle()
#increased the speed
painter.speed(20)
screen = trtl.Screen()
#changed the background color of the canvas
#to sky blue
screen.bgcolor("#87CEEB")

#moved the starting point from the origin
#to make the house centered
painter.goto(-150,35)
#function output the (x,y) values of any click
#very useful for the turtle to jump to places
def show_position(x, y):
    print(f"({x}, {y})")
trtl.onscreenclick(show_position)

#windows for the side of the house
def window():
    painter.pendown()
    painter.forward(105)
    painter.right(135)
    painter.forward(50)
    painter.right(45)
    painter.forward(105)
    painter.right(135)
    painter.forward(50)
    painter.end_fill()

#car rectangles (body and windows of car)
def car(painter, width, height, color):
    painter.fillcolor(color)
    painter.begin_fill()
    for i in range(2):
        painter.forward(width)
        painter.right(90)
        painter.forward(height)
        painter.right(90)
    painter.end_fill()

#car wheels/tires
def wheel(t, radius, color):
    painter.fillcolor(color)
    painter.begin_fill()
    painter.circle(radius)
    painter.end_fill()

#function to draw the people in the family
def person(x, y, color, height):
    painter.penup()
    painter.goto(x, y)
    painter.pendown()
    painter.color(color)

    #head of the person
    painter.begin_fill()
    painter.circle(20)
    painter.end_fill()

    #body of the person
    painter.right(90)
    painter.forward(height)

    #arms of the person
    painter.right(30)
    painter.forward(30)
    painter.backward(30)
    painter.left(60)
    painter.forward(30)
    painter.backward(30)
    painter.right(30)

    #legs of the person
    painter.forward(20)
    painter.right(30)
    painter.forward(30)
    painter.backward(30)
    painter.left(60)
    painter.forward(30)
    painter.backward(30)
    painter.right(30)

#front of the house
painter.fillcolor("#e1d5c2")
painter.begin_fill()
for i in range(4):
    painter.forward(150)
    painter.right(90)
    i += 1
painter.end_fill()

#side of the house
painter.penup()
painter.begin_fill()
painter.forward(150)
painter.left(45)
painter.pendown()
painter.forward(250)
painter.right(135)
painter.forward(150)
painter.right(45)
painter.forward(250)
painter.right(135)
painter.forward(150)
painter.end_fill()

#roof of the house
painter.fillcolor("#747c87")
painter.begin_fill()
painter.left(30)
painter.forward(150)
painter.left(120)
painter.forward(150)
painter.left(120)
painter.forward(150)
painter.left(45)
painter.forward(250)
painter.left(80)
painter.forward(125)
painter.left(95)
painter.forward(235)
painter.end_fill()

#door in front of the house
painter.left(45)
painter.penup()
painter.forward(282)
painter.right(90)
painter.forward(30)
painter.right(85)
painter.pendown()
painter.fillcolor("#5C4033")
painter.begin_fill()
painter.forward(75)
painter.right(90)
painter.forward(105)
painter.right(90)
painter.forward(75)
painter.end_fill()
painter.right(90)
painter.forward(52.5)
painter.right(90)
painter.forward(75)

#window split into four in front of the house
painter.fillcolor("#ADD8E6")
painter.penup()
painter.forward(15)
painter.right(90)
painter.forward(52.5)
painter.left(90)
painter.pencolor("white")
painter.pendown()
painter.begin_fill()
painter.forward(50)
painter.left(90)
painter.forward(105)
painter.left(90)
painter.forward(50)
painter.left(90)
painter.forward(105)
painter.left(90)
painter.end_fill()
painter.forward(25)
painter.left(90)
painter.forward(105)
painter.left(90)
painter.forward(25)
painter.left(90)
painter.forward(52.5)
painter.left(90)
painter.forward(50)
painter.right(90)

#window on the left on the side of the house
painter.penup()
painter.goto(11,29)
painter.begin_fill()
painter.left(45)
window()

#window on the right of the side of the house
painter.penup()
painter.goto(95, 115)
painter.begin_fill()
painter.right(45)
window()

#garage (rectangle) on the side of the house
painter.pencolor("black")
painter.fillcolor("#5C4033")
painter.begin_fill()
painter.penup()
painter.goto(11, -25)
painter.pendown()
painter.right(180)
painter.forward(77)
painter.left(135)
painter.forward(225)
painter.left(45)
painter.forward(77)
painter.left(135)
painter.forward(225)
painter.end_fill()

painter.penup()
painter.goto(240, -53)
painter.right(45)
painter.pendown()

#main body of the car
car(painter, 100, 50, "#50C878")

#two windows on the car
painter.penup()
painter.goto(232, -26)
painter.pendown()
car(painter, 30, 20, "white")
painter.penup()
painter.goto(177, -26)
painter.pendown()
car(painter, 30, 20, "white")

#wheels on the bottom of the car
painter.penup()
painter.goto(161, -42)
painter.pendown()
wheel(painter, 10, "black")
painter.penup()
painter.goto(218, -41)
painter.pendown()
wheel(painter, 10, "black")

painter.penup()
painter.goto(190, -3)
painter.left(90)
painter.pendown()
painter.forward(50)

#draw sun
painter.penup()
painter.goto(-301, 200)
painter.pendown()
painter.color("#FFD700")
painter.begin_fill()
painter.circle(50)
painter.end_fill()

painter.penup()
painter.goto(-251, 200)
painter.pendown()
painter.color("#FFA500")

#draw 12 rays for the sun
for i in range(12):
    painter.penup()
    painter.goto(-251, 200)
    painter.forward(50)
    painter.pendown()
    painter.forward(25)
    painter.penup()
    painter.backward(50)
    painter.left(30)
    i += 1

#draw mom
painter.left(90)
person(100, -110, "#FFC0CB", 50)

#reset orientation
painter.setheading(0)

# draw dad
person(150, -110, "#000080", 75)

#reset orientation
painter.setheading(0)

#draw daughter
person(200, -110, "#FFDAB9", 25)

wn = trtl.Screen()
wn.mainloop()
