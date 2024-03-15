import turtle

length = 10
angle = 90
turtle.hideturtle()
turtle2 = turtle.Turtle()
for _ in range(10):
  turtle.forward(length+length)
  turtle.right(angle)
  length = length + 10

for _ in range(10):
  turtle2.circle(length+length)
  length = length + 10
input()