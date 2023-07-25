with open("data") as f:
    data = [i for i in f.read().split("\n")]

def FuncPartI(_data):
    alphabet = [i for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    tot = 0
    for backpack in _data:
        seen_letters = ""
        for letter in backpack[:int(len(backpack)/2)]:
            if letter in backpack[int(len(backpack)/2):] and letter not in seen_letters:
                tot += alphabet.index(letter)+1
                seen_letters += letter
    return tot

def FuncPartII(_data):
    alphabet = [i for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    tot = 0
    for i in range(0, len(_data), 3):
        if not i+2 > len(_data)-1:
            for letter in alphabet:
                if letter in _data[i] and letter in _data[i+1] and letter in _data[i+2]:
                    tot += alphabet.index(letter) + 1
    return tot    

if __name__ == "__main__":
    print("--Part 1--", "Result:", FuncPartI(data))
    print("--Part 2--", "Result:", FuncPartII(data))