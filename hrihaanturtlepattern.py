import turtle

screen = turtle.Screen()
screen.bgcolor('black')

class TurtlePattern:
    def __init__(self):
        self.shapes = ["turtle", "triangle", "circle", "arrow", "square", "classic", "triangle", "turtle", 
                       "arrow", "circle", "square", "classic", "arrow", "circle", "triangle", "turtle"]
        self.colors = ["violet", "yellow", "cyan", "pink", "green", "blue", "red", "orange", "gold", 
                       "silver", "magenta", "purple", "yellow", "green", "blue", "red"]
        self.turtles = []
        
        for x in range(len(self.shapes)):
            t = turtle.Turtle()
            t.shape(self.shapes[x])
            t.penup()
            t.speed(0)
            t.color(self.colors[x])
            self.turtles.append(t)

    def draw(self):
        x = 0
        y = 0
        heading = 90
        distance = 60
        
        for t in self.turtles:
            t.goto(x, y)
            t.pendown()
            t.setheading(heading)
            t.right(60)
            t.forward(distance)
            
            x = t.xcor()
            y = t.ycor()
            heading = t.heading()
            distance += 5


pattern = TurtlePattern()
pattern.draw()
screen.mainloop()
