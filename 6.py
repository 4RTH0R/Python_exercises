import turtle

t = turtle.Turtle()
t.fillcolor("red")
t.begin_fill()
for _ in range(6):
  t.forward(100)
  t.left(60)
t.end_fill()

input()