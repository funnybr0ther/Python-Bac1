import turtle   
import time        # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
mamene = turtle.Turtle()    # Create a turtle, assign to mamene

         # Tell mamene to move forward by 50 units 
mamene.width(8)
mamene.left(90)
mamene.color("green")
mamene.circle(45,360)
mamene.right(180)
mamene.circle(45,450)
mamene.right(180)
mamene.left(90)
mamene.forward(200)
mamene.left(180)
mamene.circle(45,-180)
mamene.left(90)
mamene.forward(90)
mamene.left(180)
mamene.forward(90)
mamene.right(90)
mamene.forward(200)
mamene.penup()
mamene.right(90)
mamene.forward(45)
mamene.right(90)
mamene.forward(215)
mamene.pendown()
mamene.forward(30)
wn.mainloop()             # Wait for user to close window