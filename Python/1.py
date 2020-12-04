
    def turn_right(self):
        self.reset_orientation()
        self.orientation += 1

    def move(self):
        if(self.orientation == 0):  # right
            self.cur_x += 1
            if(self.cur_x + 1 > self.rows):
                self.cur_x = 0

        elif(self.orientation == 1):  # down
            self.cur_y += 1
            if(self.cur_y + 1 > self.columns):
                self.cur_y = 0
        elif(self.orientation == 2):  # left
            self.cur_x -= 1
            if(self.cur_x - 1 < 0):
                self.cur_x = self.rows

        elif(self.orientation == 3):  # up
            self.cur_y -= 1
            if(self.cur_y - 1 < 0):
                self.cur_y = self.columns
        self.canvas[self.cur_y][self.cur_x] += 1

    def spawn_at(self, rows, columns):
        self.canvas[columns][rows] = self.canvas[columns][rows] + 1
        self.curr_x = rows
        self.curr_y = columns

    def print_turtle(self):
        for line in turtle.canvas:
            print(line)

class SimpleCanvas():
    def __init__(self, canvas, array):
        self.pixel = canvas
        self.array = array
    def draw(self):
        maxx = max(map(max,self.canvas))
        intesity = 0
        for rows in range(len(canvas)):
          for columns in range(len(canvas[0]):
            intensisty = canvas[rows][columns] / maxx   
            if(intesity == 0):
               self.pixel[rows][columns] = self.array[0]
            elif(0 < intesity <= 0.3):
               self.pixel[rows][columns] = self.array[1]
            elif(0.3 < intesity <= 0.6):
               self.pixel[rows][columns] = self.array[2]
            elif(0.6 < intesity <= 1):
               self.pixel[rows][columns] = self.array[3]

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
