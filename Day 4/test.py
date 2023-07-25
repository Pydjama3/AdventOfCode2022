ll = [[[int(i) for i in y.split("-")] for y in x.split(",")] for x in open("data").read().strip().split('\n')]

c = 0

for l in ll:
    first_elf = set(range(l[0][0], l[0][1]+1))
    second_elf = set(range(l[1][0], l[1][1]+1))
    print(l[0], l[1])
    if first_elf <=second_elf or second_elf <= first_elf:
        c += 1

print(c)