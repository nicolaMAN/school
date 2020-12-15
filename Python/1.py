class Turtle:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.canvas = [[0 for i in range(columns)] for j in range(rows)]
        self.x = None
        self.y = None
        self.orientation = 0
        
    def turn_right(self):
        self.orientation += 1
        if(self.orientation > 3):
            self.orientation = 0
    def turn_left(self):
        self.orientation -= 1
        if(self.orientation < 0):
            self.orientation = 3
    def move(self):
        if(self.x == None and self.y == None):
            raise RuntimeError
            
        if(self.orientation == 0):  # right
            self.x += 1
            if(self.x + 1 > self.rows):
                self.x = 0
        elif(self.orientation == 1):  # down
            self.y += 1
            if(self.y + 1 > self.columns):
                self.y = 0
        elif(self.orientation == 2):  # left
            self.x -= 1
            if(self.x - 1 < 0):
                self.x = self.rows - 1
        elif(self.orientation == 3):  # up
            self.y -= 1
            if self.y == 0:
                self.y = self.columns - 1
        self.canvas[self.y][self.x] += 1
    def spawn_at(self, rows, columns):
        self.canvas[columns][rows] = self.canvas[columns][rows] + 1
        self.x = rows
        self.y = columns
class SimpleCanvas():
    def __init__(self, canvas, array):
        self.pixel = []
        self.canvas = canvas
        self.array = array
    def draw(self):
        maxx = max(map(max,self.canvas))
        intensity = 0
        self.pixel = [[0 for i in range(len(self.canvas))] for j in range(len(self.canvas[0]))]
        for rows in range( len (self.canvas) ):
            for columns in range(len (self.canvas[0])):
                intensity = self.canvas[rows][columns] / maxx
                if(intensity == 0):
                    self.pixel[rows][columns] = self.array[0]
                elif(0 < intensity <= 0.3):
                    self.pixel[rows][columns] = self.array[1]
                elif(0.3 < intensity <= 0.6):
                    self.pixel[rows][columns] = self.array[2]
                elif(0.6 < intensity <= 1):
                    self.pixel[rows][columns] = self.array[3] 
        string = [0 for i in range(len(self.canvas))]
        for i in range(len(self.canvas)):
            string[i]= ''.join(self.pixel[i])
        res = ""
        res = "\n".join(string)
        return res
# nqkuv komentar
turtle = Turtle(3, 3)
turtle.spawn_at(0, 0)
for i in range(9):
    turtle.move()
turtle.turn_right()
for i in range(4):
    turtle.move()
turtle.turn_left()
turtle.move()
turtle.move()
turtle.turn_right()
turtle.move()
canvas = SimpleCanvas(turtle.canvas, [' ', '*', '@', '#'])
print(canvas.draw())
