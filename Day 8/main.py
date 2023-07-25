with open('data') as f:
    data = [[int(j) for j in i] for i in f.read().splitlines()]

def FuncPartI(_data):
    trees = []
    max_heights = {"x_way":[-1 for i in data], "r_x_way":[-1 for i in data], "y_way":[-1 for i in data[0]], "r_y_way":[-1 for i in data[0]]}
    for y in range(len(_data)):
        for x in range(len(_data[y])):
            if max_heights["y_way"][y]<_data[x][y]:
                if [x, y] not in trees:
                    trees.append([x, y])
                max_heights["y_way"][y] = _data[x][y]
            if max_heights["x_way"][y]<_data[y][x]:
                if [y,x] not in trees:
                    trees.append([y, x])
                max_heights["x_way"][y] = _data[y][x]
            if max_heights["r_y_way"][y]<_data[y][len(_data[y])-x-1]:
                if [y, len(_data[y])-x-1] not in trees:
                    trees.append([y, len(_data[y])-x-1])
                max_heights["r_y_way"][y] = _data[y][len(_data[y])-x-1]
            if max_heights["r_x_way"][y]<_data[len(_data)-x-1][y]:
                if [len(_data)-x-1, y] not in trees:
                    trees.append([len(_data)-x-1, y])
                max_heights["r_x_way"][y] = _data[len(_data)-x-1][y]
            # print(trees)
            # print(max_heights)
            # print(y, x)
            # print("----------------------------------------------------------------")
    return len(trees)

print("--Part 1--", "Result:", FuncPartI(data))