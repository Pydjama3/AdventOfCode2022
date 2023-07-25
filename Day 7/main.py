with open("data") as f:
    data = [i for i in f.read().split("\n")]
    # print(data)

def FuncPartI(_data):
    path = []
    dir_dict = {}
    for line in _data:
        if line.startswith("$ cd"):
            if line=="$ cd ..":
                path.pop()
            else:
                path.append(line.split(" ")[-1])
                dir_dict["/".join(path)+"/"] = 0
        elif line.split(' ')[0].isnumeric():
            dir_dict["/".join(path)+"/"]+= int(line.split(" ")[0])
    for key in dir_dict:
        path = key
        # print(key, dir_dict, currentpath)
        while len(path) > 2:
            parent = path[:path[:path.rfind("/")].rfind("/")+1]
            dir_dict[parent] += dir_dict[key]
            path = parent
    a = 0
    for i in dir_dict:
        if dir_dict[i]<=100000:
            a+=dir_dict[i]
    return a, dir_dict

def FuncPartII(_data):
    _, dir_dict = FuncPartI(_data)
    free_storage = 70000000 - dir_dict["//"]
    to_free = 30000000 - free_storage
    dir_to_del = dir_dict["//"]
    for i in dir_dict:
        if dir_dict[i]>=to_free and dir_dict[i] < dir_to_del:
            dir_to_del = dir_dict[i]
    return dir_to_del


print("--Part 1--", "Result:", FuncPartI(data)[0])
print("--Part 2--", "Résult:", FuncPartII(data))