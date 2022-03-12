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

    print(maze)
    return maze


pt_start = (start_x, start_y)
print(pt_start)

createMaze()