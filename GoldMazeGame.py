
import turtle
import math
import random

Background_Pic = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/B.gif"
GameOver = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/GameOverBackground.gif"
# Player_Left = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/left.gif"
# Player_Right = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/right.gif"
# Player_Up = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/up.gif"
# Player_Down = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/down.gif"
Player_Skeleton = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/player.gif"
Enemy_Left = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/enemyGhostLeft.gif"
Enemy_Right = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/enemyGhostRight.gif"
Brick_Pic = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/Brick.gif"
OpenTreasure_Pic = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/OpenTreasure.gif"
ClosedTreasure_Pic = "/home/lenovo/PESU Sem - 1/MazeGame/Sprites/ClosedTreasure.gif"

wn = turtle.Screen()
wn.bgpic(Background_Pic)
wn.bgcolor('black')
wn.title('Get That Gold')
wn.setup(700, 700)
wn.tracer(0)

for image in [Player_Skeleton, GameOver, Background_Pic,
            # Player_Left, Player_Right, Player_Up, Player_Down,
            Brick_Pic, OpenTreasure_Pic,  ClosedTreasure_Pic, Enemy_Left, Enemy_Right]:
    turtle.register_shape(image)


class Wall(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        # self.shape(Brick_Pic)
        self.shape('square')
        self.color('grey')
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(Player_Skeleton)
        self.penup()
        self.speed(0)
        self.points = 0
        self.lives = 3

    def take_next_step(self, next_x, next_y):
        if (next_x, next_y) not in walls:
            self.goto(next_x, next_y)

    def move_up(self):
        self.take_next_step(self.xcor(), self.ycor() + 24)
        # self.shape(Player_Up)

    def move_down(self):
        self.take_next_step(self.xcor(), self.ycor() - 24)
        # self.shape(Player_Down)

    def move_right(self):
        self.take_next_step(self.xcor() + 24, self.ycor())
        # self.shape(Player_Right)

    def move_left(self):
        self.take_next_step(self.xcor() - 24, self.ycor())
        # self.shape(Player_Left)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt(a**2 + b**2)
        return True if distance == 0 else False


class Enemy(turtle.Turtle):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(Enemy_Left)
        self.penup()
        self.speed(0)
        self.points = 20
        self.goto(x, y)
        self.direction = random.choice(("L", "R", "U", "D"))
        if self.direction == "L":
            self.shape(Enemy_Left)
        elif self.direction == "R":
            self.shape(Enemy_Right)

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

class Exit(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("black")
        self.penup()
        self.speed(0)

    def isLevelDone(self):
        wn.clearscreen()
        wn.bgpic(Background_Pic)
        wn.tracer(0)
        setup_maze(levels[2])



class Lives(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.penup()
        self.speed(0)
        self.setposition(100, 320)
        self.hideturtle()
        self.lifecount = 'Lives Remaining: {}'.format(player.lives)

    def showLives(self):
        self.write(self.lifecount, False, align='left', font=('Times New Roman', 14, 'bold'))


class Points(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.penup()
        self.speed(0)
        self.setposition(-300, 320)
        self.hideturtle()

    def showPoints(self):
        self.write('Points: {}'.format(player.points), False, align='left', font=('Times New Roman', 14, 'bold'))


def setup_maze(level):

    livesBox.showLives()
    pointsBox.showPoints()

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

            if character == 'I':
                exit.goto(x_coordinate, y_coordinate)
                exit.x_cor, exit.y_cor = x_coordinate, y_coordinate
                walls.append((exit.x_cor, exit.y_cor))

def setup_level(level):

    setup_maze(levels[level])

    wn.onkey(player.move_down, "Down")
    wn.onkey(player.move_up, "Up")
    wn.onkey(player.move_left, "Left")
    wn.onkey(player.move_right, "Right")
    wn.listen()

    for enemy in enemies:
        turtle.ontimer(enemy.move_enemy, t=120)

block = Wall()
player = Player()
livesBox = Lives()
pointsBox = Points()
exit = Exit()
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
    "X  X     X     X        X",
    "X  X  XXXXXXXXXXXXXXXX  X",
    "X     XT             E  X",
    "X  XXXX  X  XXXXXXXXXX  X",
    "X  X  X  X  X     X     X",
    "X  X  X  X  XXXX  X  XXXX",
    "X  XE    X     XT       X",
    "X  XXXX  XXXX  XXXXXXX  X",
    "X     X     X        X  X",
    "XXXX  XXXXXXX  XXXX  XXXX",
    "X  X E      X  XE X     X",
    "X  XXXXXXX  X  X  XXXX  X",
    "X  XT       X     X     X",
    "X  X  XXXXXXXXXXXXX  X  X",
    "X     X     X        X  X",
    "X  XXXX  X  X  XXXXXXX  X",
    "X     E  X     X        I",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]
level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "IT         EX           X",
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
    "X  X  X     X TX  X  X  X",
    "XE X  XXXX  XXXX  X X   X",
    "X  X     E  X     X     X",
    "X  X  XXXXXXX  XXXXXXX  X",
    "X  X     XT         EX  X",
    "X  XXXX  XXXXXXXXXXXXX  X",
    "X       E             X X",
    "XXXXXXX  X  XXXXXXX  X  X",
    "X        X     X  XE   TX",
    "X  XXXXXXXXXX  X  XXXXXXX",
    "XE                     PX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

levels.append(level_1)
levels.append(level_2)

setup_level(1)

print(walls)
print((exit.xcor(), exit.ycor()))
print((exit.xcor(), exit.ycor()) in walls)
while True:

    if len(treasure) == 0:
        if (exit.xcor(), exit.ycor()) in walls:
            walls.remove((exit.xcor(), exit.ycor()))
        if player.is_collision(exit):
            exit.isLevelDone()
            setup_level(2)

    for reward in treasure:

        if player.is_collision(reward):
            reward.shape(OpenTreasure_Pic)
            player.points += reward.points
            # if reward.points == 100:
                # turtle.write('Gold Acquired!', False, align='center', font=('Times New Roman', 60, 'bold'))
            pointsBox.clear()
            pointsBox.showPoints()
            print("Player Points: {}".format(player.points))
            treasure.remove(reward)

    for enemy in enemies:

        if player.is_collision(enemy):
            player.lives -= 1
            livesBox.lifecount = 'Lives Remaining: {}'.format(player.lives)
            livesBox.clear()
            livesBox.showLives()
            enemy.destroy()

            if player.lives == 0:
                print("Player Dead")
                wn.clearscreen()
                wn.bgpic(GameOver)
                turtle.hideturtle()
                turtle.color('white')
                turtle.write('Game Over', False, align='center', font=('Times New Roman', 50, 'bold'))

    wn.update()

wn.mainloop()
wn.done()
