import queue


with open ("./maps/rect_01.map", 'r') as map:
    matrice = map.read().split("\n")

matrix = []

start_x = 0
start_y = 0
end_x = 0
end_y = 0

x = 0

for line in matrice:
    y = 0
    if x == 0 or x > len(matrix) - 1:
        matrix.append([])
    for value in line:
        if value == '1':
            start_x = x
            start_y = y

        if value == '2':
            end_x = x
            end_y = y

        matrix[x].append(value)
        y += 1
    x += 1


def createMaze():
    maze = []
    for i in range(0, y - 1):
        maze.append(matrix[i])
    return maze

pt_start = (start_x, start_y)
print(pt_start)

createMaze()

def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "1":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "1":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "*"):
            return False

    return True


def findEnd(maze, moves):
    start = 0
    for x, pos in enumerate(maze[0]):
        if pos == "1":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "2":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False

nums = queue.Queue()
nums.put("")
add = ""
maze = createMaze()

while not findEnd(maze, add):
    add = nums.get()
    # print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)