import turtle

screen = turtle.Screen()
screen.bgcolor("pink")

screen.title("Turtle")

myPen = turtle.Turtle()
size= 0

while True:
    
    for i in range(4):
        myPen.fd(size+1)
        myPen.left(90)
        size= size-2
    size= size+1