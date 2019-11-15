from random import shuffle, randrange
import sys

def make_maze(w=8, h=12):

    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["X  "] * w + ['X'] for _ in range(h)] + [[]]
    hor = [["XXX"] * w + ['X'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                hor[max(y, yy)][x] = "X  "
            if yy == y:
                ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s


if __name__ == '__main__':
    print(make_maze())
