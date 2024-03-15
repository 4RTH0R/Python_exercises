import turtle

#Fundo do desenho
t3 = turtle.Turtle()
t3.speed(1)
t3.fillcolor("yellow")
t3.begin_fill()
t3.right(100)
t3.circle(50)
t3.end_fill()

#Borda do desenho
t2 = turtle.Turtle()
t2.speed(2)
t2.pensize(10)
t2.right(100)
t2.circle(50)

#Desenho
t = turtle.Turtle()
t.speed(10)
t.fillcolor("purple")
t.begin_fill()
for _ in range(6):
  t.radians()
  t.forward(100)
  t.left(60)
t.end_fill()
t.pensize(10)
t.right(121)

input()