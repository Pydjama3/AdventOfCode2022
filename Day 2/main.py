with open('data') as f:
    data = [i for i in f.read().split("\n")]

    for k in range(len(data)):
        data[k] = data[k].split(' ')

def FuncPartI(_data):
    # rock, paper, sciscors
    elves_references = {'A':1,'B':2,'C':3, 'X':1, 'Y':2, 'Z':3}
    score = 0
    for i in _data:
        if elves_references[i[0]]%3 + 1 == elves_references[i[1]]:
            score += 6
        elif elves_references[i[0]] == elves_references[i[1]]:
            score += 3
        else:
            score += 0
        score += elves_references[i[1]]
    return score

def FuncPartII(_data):
    elves_references = {'A':1,'B':2,'C':3, 'X':-1, 'Y':0, 'Z':1}
    my_references = {"X":0, "Y":3, "Z":6}
    score = 0
    for i in _data:
        score += my_references[i[1]]
        score += (elves_references[i[0]]-1+elves_references[i[1]])%3 + 1
    return score        

if __name__ == "__main__":
    print("--Part 1--","Result:",FuncPartI(data))
    print("--Part 2--","Result:",FuncPartII(data))