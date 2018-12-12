import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex

         # Tell alex to move forward by 50 units
while 1 == True:
    alex.left(90)  
    alex.color("green")
    alex.circle(45,360)
    alex.right(180)
    alex.circle(45,450)
    alex.right(180)
    alex.left(90)
    alex.forward(200)
    alex.left(180)
    alex.circle(45,-180)
    alex.left(90)
    alex.forward(90)
    alex.left(180)
    alex.forward(90)
    alex.right(90)
    alex.forward(200)



wn.mainloop()             # Wait for user to close window