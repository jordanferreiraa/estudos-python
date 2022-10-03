import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.width(2)
t.speed(15)

col = ('yellow','green','red','blue')

for i in range(300):
  t.pencolor(col[i%4])
  t.forward(i*4)
  t.right(137)