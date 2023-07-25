with open("data") as f:
    data = [[[int(i) for i in j.split("-")] for j in k.split(",")] for k in f.read().strip().split('\n')] # [[["a","b"], ["c","d"]]]
    print(len(data))

def FuncPartI(_data):
    tot = 0
    for first, second in _data:
        tot+= 1 if (first[0]<=second[0] and first[1]>=second[1]) or (first[0]>=second[0] and first[1]<=second[1]) else 0
    return tot

def FuncPartII(_data):
    tot = 0
    for first, second in _data:
        first_range = set(range(first[0], first[1]+1))
        second_range = set(range(second[0], second[1]+1))
        if first_range.intersection(second_range)!=set():
            tot+=1
    return tot

print("--Part 1--", "Result:", FuncPartI(data))
print("--Part 2--", "Result:", FuncPartII(data))