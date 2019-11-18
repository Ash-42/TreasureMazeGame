
import turtle
import math
import random

Background_Pic = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/Bck1_2.gif"
Player_Left = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/left.gif"
Player_Right = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/right.gif"
Player_Up = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/up.gif"
Player_Down = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/down.gif"
# Enemy_Left =
# Enemy_Right =
Brick_Pic = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/Brick.gif"
OpenTreasure_Pic = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/OpenTreasure.gif"
ClosedTreasure_Pic = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/ClosedTreasure.gif"

wn = turtle.Screen()
# wn.reset()
# wn.setworldcoordinates(-288, -312, 312, 288)
wn.bgpic(Background_Pic)
wn.title('Get That Gold')
wn.setup(700, 700)
wn.tracer(0)
# wn.screensize()

for image in [Background_Pic, Player_Left, Player_Right, Player_Up, Player_Down, Brick_Pic, OpenTreasure_Pic,  ClosedTreasure_Pic]:
    turtle.register_shape(image)


class Wall(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(Brick_Pic)
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(Player_Right)
        self.penup()
        self.speed(0)
        self.points = 0
        self.lives = 3

    def take_next_step(self, next_x, next_y):
        if (next_x, next_y) not in walls:
            self.goto(next_x, next_y)

    def move_up(self):
        self.take_next_step(self.xcor(), self.ycor() + 12)
        self.shape(Player_Up)

    def move_down(self):
        self.take_next_step(self.xcor(), self.ycor() - 12)
        self.shape(Player_Down)

    def move_right(self):
        self.take_next_step(self.xcor() + 12, self.ycor())
        self.shape(Player_Right)

    def move_left(self):
        self.take_next_step(self.xcor() - 12, self.ycor())
        self.shape(Player_Left)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt(a**2 + b**2)
        return True if distance < 5 else False


class Enemy(turtle.Turtle):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('red')
        self.penup()
        self.speed(0)
        self.points = 20
        self.goto(x, y)
        self.direction = random.choice(("L", "R", "U", "D"))

    def move_enemy(self):
        next_x = self.xcor() + 24*(self.direction == "L")\
                 - 24*(self.direction == "R")
        next_y = self.ycor() + 24*(self.direction == "U")\
            - 24*(self.direction == "D")

        if (next_x, next_y) not in walls:
            self.goto(next_x, next_y)
        else:
            self.direction = random.choice(("L", "R", "U", "D"))
        turtle.ontimer(self.move_enemy, t=random.randint(100, 300))

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Treasure(turtle.Turtle):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(ClosedTreasure_Pic)
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.destroy


class Score(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("black")
        self.penup()
        self.speed()


def setup_maze(level):

    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            x_coordinate = -288 + (x * 24)
            y_coordinate = 288 - (y * 24)

            if character == 'X':
                block.goto(x_coordinate, y_coordinate)
                block.stamp()
                walls.append((x_coordinate, y_coordinate))

            if character == 'P':
                player.goto(x_coordinate, y_coordinate)

            if character == 'T':
                reward = random.choice(('Gold', 'Silver', 'Bronze'))
                if reward == 'Gold':
                    Treasure.points = 100
                elif reward == 'Silver':
                    Treasure.points = 60
                elif reward == 'Bronze':
                    Treasure.points = 30
                treasure.append(Treasure(x_coordinate, y_coordinate))

            if character == 'E':
                enemies.append(Enemy(x_coordinate, y_coordinate))


block = Wall()
player = Player()
# reward = Reward()
treasure = []
enemies = []
walls = []
levels = [""]
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP       X     X    E   X",
    "XXXXXXX  X  X  X  XXXX  X",
    "X        X EX  X  X  X  X",
    "X  X  XXXXXXX  X  X  X  X",
    "X  X  X     X  X  X     X",
    "X  XXXX  X  X  X  XXXXXXX",
    "X  X     X     XT       X",
    "X  X  XXXXXXXXXXXXXXXX  X",
    "X     X              E  X",
    "X  XXXX  X  XXXXXXXXXX  X",
    "X  X  X  X  XT    X     X",
    "X  X  X  X  XXXX  X  XXXX",
    "X  XE    X     X        X",
    "X  XXXX  XXXX  XXXXXXX  X",
    "X     X     X        X  X",
    "XXXX  XXXXXXX  XXXX  XXXX",
    "X  X E      X  X TX     X",
    "X  XXXXXXX  X  X  XXXX  X",
    "X  X        X     X     X",
    "X  X  XXXXXXXXXXXXX  X  X",
    "X     X     X        X  X",
    "X  XXXX  X  X  XXXXXXX  X",
    "X     E  X     X        X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]
level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XT         EX           X",
    "X  XXXXXXX  XXXXXXXXXX  X",
    "X       EX     X     X  X",
    "X  XXXX  XXXX  X  X  X  X",
    "X  X  XE X  X     X    TX",
    "X  X  X  X  XXXX  XXXXXXX",
    "X     X  X     X  XE    X",
    "X  XXXX  X  XXXX  XXXX  X",
    "X  X     XE       X     X",
    "XXXX  XXXXXXXXXX  X  XXXX",
    "X     X        X  X  X  X",
    "X  XXXX  X  X TX  X  X  X",
    "XE XXXXXXX  XXXX  X X  X",
    "X  X     E  X     X     X",
    "X  X  XXXXXXX  XXXXXXX  X",
    "X  X     XT         EX  X",
    "X  XXXX  XXXXXXXXXXXXX  X",
    "X       E             X  X",
    "XXXXXXX  X  XXXXXXX  X  X",
    "X        X     X  XE   TX",
    "X  XXXXXXXXXX  X  XXXXXXX",
    "XE                     PX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

levels.append(level_1)
levels.append(level_2)

setup_maze(levels[1])

wn.onkey(player.move_down, "Down")
wn.onkey(player.move_up, "Up")
wn.onkey(player.move_left, "Left")
wn.onkey(player.move_right, "Right")
wn.listen()

for enemy in enemies:
    turtle.ontimer(enemy.move_enemy, t=120)

while True:
    for reward in treasure:
        if player.is_collision(reward):
            reward.shape(OpenTreasure_Pic)
            player.points += reward.points
            print("Player Points: {}".format(player.points))
            treasure.remove(reward)

    for enemy in enemies:
        if player.is_collision(enemy):
            player.lives -= 1
            if player.lives == 0:
                print("Player Dead")
                # turtle.clearscreen()


    wn.update()

wn.mainloop()
