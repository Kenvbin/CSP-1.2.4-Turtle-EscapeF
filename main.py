import turtle as t
import random as r

lengthygenthy = 15
path_width = 5

t.pensize(10)
t.speed(0)


def doorlore():

  t.forward(30)
  t.penup()
  t.forward(path_width*7)
  t.pendown()

def border_lore():
  t.forward(40)
  t.left(90)
  t.forward(path_width*2)
  t.back(path_width*2)
  t.right(90)

def spiralhal(howmany):
  global lengthygenthy, randomise
  for i in range(howmany):
    t.forward(lengthygenthy)
    t.right(90)
    lengthygenthy = lengthygenthy + 15
    doorlore()

spiralhal(20)

wm = t.getscreen()
wm.mainloop()