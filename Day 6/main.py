with open("data") as f:
    data = f.read().strip()

def FuncPartI(_data):
    for pos in range(len(_data)-4):
        if sum([_data[pos:pos+4].count(i) for i in _data[pos:pos+4]]) == 4:
            return pos+4

def FuncPartII(_data):
    for pos in range(len(_data)-14):
        if sum([_data[pos:pos+14].count(i) for i in _data[pos:pos+14]]) == 14:
            return pos+14

if __name__ == "__main__":
    print("--Part 1--", "Result:", FuncPartI(data))
    print("--Part 2--", "Result:", FuncPartII(data))