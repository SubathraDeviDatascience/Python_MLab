import turtle
def draw_bear():
    turtle.speed(2)
    turtle.bgcolor("lightblue")
    #Draw the bear’s head
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()
    #Draw the bear’s ear
    turtle.penup()
    turtle.goto(-30, 50)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(30, 50)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
  
  # Draw the bear’s eyes
    turtle.penup()
    turtle.goto(-20, 10)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(8)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(20, 10)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(8)
    turtle.end_fill()
    #Draw the bear’s nose
    turtle.penup()
    turtle.goto(0, -5)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    #Draw the bear’s Smiling mouth
    turtle.penup()
    turtle.goto(-20, -20)
    turtle.pendown()
    turtle.color("black")
    turtle.width(3)
    turtle.right(90) 
    turtle.circle(20, 180)
    #Draw the semicircle for a smile
   # Hide the turtle
    turtle.hideturtle()
    # Keep the window open
    turtle.done()
#Draw the bear
draw_bear()
