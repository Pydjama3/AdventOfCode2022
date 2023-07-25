from copy import deepcopy

with open("data") as f:
    raw_data = f.read().split("\n")
    up_to = 0
    for i in range(len(raw_data)):
        if raw_data[i].startswith("move"):
            up_to = i
            break
    crane_stacks = {}
    for i in range(up_to-2):
        for j in range(0, len(raw_data[0]), 4):
            if raw_data[i][j+1]!=" ":
                if (j+4)//4 not in crane_stacks.keys():
                    crane_stacks[(j+4)//4] = [raw_data[i][j+1]]
                else:
                    crane_stacks[(j+4)//4].append(raw_data[i][j+1])
    actions=[[int(i.split(" ")[1]), int(i.split(" ")[3]), int(i.split(" ")[5])] for i in raw_data[up_to:]]
    crane_stacks_bis = deepcopy(crane_stacks)
    actions_bis = deepcopy(actions)

def FuncPartI(_cranes, _actions):
    for action in _actions:
        for i in range(action[0]):
            _cranes[action[2]].insert(0, _cranes[action[1]].pop(0))
    return ''.join([_cranes[i+1][0] for i in range(len(_cranes.keys()))])

def FuncPartII(_cranes, _actions):
    for action in _actions:
        for i in range(action[0]):
            _cranes[action[2]].insert(0, _cranes[action[1]].pop(action[0]-i-1))
    return ''.join([_cranes[i+1][0] for i in range(len(_cranes.keys()))])

if __name__ == "__main__":
    print("--Part 1--","Result:", FuncPartI(crane_stacks, actions))
    print("--Part 2--","Result:", FuncPartII(crane_stacks_bis, actions_bis))