import turtle
turtle.Screen().bgcolor("orange") 
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
sides=int(input("enter the number of sides: "))
angle = 360/sides
side_length = float(input("Enter the side length: "))
for i in range(sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()
