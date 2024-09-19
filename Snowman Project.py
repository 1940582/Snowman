import turtle as trtl

#screen/background
wn = trtl.Screen()
wn.setup(width = 1920, height = 1080)
wn.bgpic("H:\maze\snow 2.png")



answer = input("Do you want to build a snowman? (y/n) ")
if (answer == 'y'):

    trtl.fillcolor("white")
    trtl.begin_fill()
    trtl.speed(0)
    trtl.pencolor("white")
    
    #base snowball
    trtl.penup()
    trtl.goto(0, -125)
    trtl.pendown()
    trtl.circle(50)

    #middle snowball
    trtl.penup()
    trtl.goto(0, -45)
    trtl.pendown()
    trtl.circle(35)

    #top snowball
    trtl.penup()
    trtl.goto(0, 15)
    trtl.pendown()
    trtl.circle(20)

    trtl.end_fill()
if (answer == 'n'):
    print("goodbye")
    quit()

answer = input("Do you want your snowman to have eyes? ")
if (answer == 'y'):

    #eyes
    trtl.pencolor("black")
    trtl.penup()
    trtl.pensize(4)
    trtl.goto(-8,40)
    trtl.pendown()
    trtl.circle(2,360)
    trtl.penup()
    trtl.goto(7,40)
    trtl.pendown()
    trtl.circle(2,360)
    trtl.hideturtle()

answer = input("Do you want your snowman to have a mouth? ")
if (answer == 'y'):

    #mouth
    trtl.penup()
    trtl.pencolor("black")
    trtl.goto(0,25)
    trtl.pendown()
    trtl.goto(0,25)
    trtl.penup()
    trtl.goto(5,27)
    trtl.pendown()
    trtl.goto(5,27)
    trtl.penup()
    trtl.goto(-5,27)
    trtl.pendown()
    trtl.goto(-5,27)
    trtl.hideturtle()

answer = input("Do you want your snowman to have a nose? ")
if (answer == 'y'):
    #snowman carrot Nose
    trtl.penup()
    trtl.setheading(60)
    trtl.goto(0,35)
    trtl.pencolor("orange")
    trtl.pensize(5)
    trtl.right(90)
    trtl.pendown()
    trtl.forward(20)
    trtl.hideturtle()

answer = input("Do you want your snowman to have arms? ")
if (answer == 'y'):
    #snowman's left arm
    trtl.pensize(5)
    trtl.penup()
    trtl.goto(-30, 5)
    trtl.setheading(60)
    trtl.pendown()
    trtl.pencolor("saddlebrown")
    trtl.goto(-100, 20)
    trtl.hideturtle()

    #snowman's right arm
    trtl.penup()
    trtl.goto(30, 5)
    trtl.setheading(60)
    trtl.pendown()
    trtl.pencolor("saddlebrown")
    trtl.goto(100, 20)
    trtl.hideturtle()

answer = input("Do you want your snowman to have buttons? ")
if (answer == 'y'):

    #buttons on middle snowball
    trtl.xcor = 0
    trtl.ycor = -5
    trtl.penup()
    trtl.goto(0, -5)
    trtl.color("black")
    trtl.pendown()
    trtl.circle(2)
    trtl.penup()
    trtl.goto(trtl.xcor, trtl.ycor-17)
    trtl.pendown()
    trtl.circle(2)
    trtl.penup()
    trtl.ycor = -20
    trtl.goto(trtl.xcor, trtl.ycor-15)
    trtl.pendown()
    trtl.circle(2)
    trtl.penup()
    trtl.hideturtle()


answer = input("Do you want to add a hat? ")
if (answer == 'y'):

    #snowman's Hat
    trtl.pencolor("black")
    trtl.fillcolor("black")
    trtl.begin_fill()

    trtl.penup()
    trtl.goto(-20,50)
    trtl.pensize(4)
    trtl.pendown()
    trtl.goto(20,50)
    trtl.goto(20,60)
    trtl.goto(10,60)
    trtl.goto(10,90)
    trtl.goto(-10,90)
    trtl.goto(-10,60)
    trtl.goto(-20,60)
    trtl.goto(-20,50)

    trtl.end_fill()

answer = input("Should your snowman have a scarf?")
if (answer == 'y'):

    trtl.pencolor("red")
    trtl.penup()
    trtl.right(120)
    trtl.goto(-18,21)
    trtl.pendown()
    trtl.pensize(8)
    trtl.circle(20,130)
    trtl.hideturtle()
    trtl.penup()
    trtl.goto(-10,13)
    trtl.pendown()
    trtl.pensize(10)
    trtl.goto(-12,-30)
    trtl.hideturtle()


wn.mainloop() 