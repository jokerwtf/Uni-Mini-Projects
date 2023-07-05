# You need to install turtle if not already installed.
import turtle as tr

class Pen(tr.Turtle):
    def __init__(self):
        tr.Turtle.__init__(self, "turtle")
        self.speed("fastest")
        self.ondrag(self.draw)
        self.traces = []
        self.traces.append(Tracer(1, 1))
    
    def draw(self, x, y):
        self.ondrag(None)
        self.goto(x, y)
        for element in self.traces:
            element.moveto(x, -y)
        self.ondrag(self.draw)

class Tracer(tr.Turtle):
    def __init__(self, dx, dy, a=0, b=0, width=1, color='red'):
        tr.Turtle.__init__(self)
        self.hideturtle()
        self.color(color)
        self.width(width)
        self.a = a
        self.b = b
        self.dx = dx
        self.dy = dy
    
    def moveto(self, x, y):
        self.goto(x * self.dx + self.a, y * self.dy + self.b)

p = Pen()
tr.mainloop()
