import random
print(
    "You are lost in uncharted lands of the world, without any help and are surrounded by dangerous creatures. "
    "The Earth has been destroyed and you are the only human left in the world. "
    "Your only hope is to make the Time Machine to travel to when the humans lived and save the Earth. "
    "This is not an easy task though, having the materials of the Time Machine so rare,"
    " and you also have to fight dangerous creatures to get to the materials. ")
damage = 1
health = 100
map = []
dangers = [0, 1, 0, 5, 0, 7, 1, 5, 1, 9, 2, 2, 2, 4, 2, 7, 3, 0, 3, 2, 3, 6, 3, 9, 4, 8, 5, 1, 5, 3, 5, 9, 6, 0, 6, 7,
           7, 2, 7, 5, 7, 9, 8, 1, 8, 8, 9, 2, 9, 4, 9, 6, 9, 7]
pos = [4, 5]
v = 0
for i in range(10):
    for o in range(10):
        map.append(i)
        map.append(o)
while True:
    print(f'damage: {damage}, health {health}, position {pos}')
    a = int(input("""
    1 for up
    2 for down
    3 for left
    4 for right"""))
    if a == 1:
        pos = [pos[0], pos[1] + 1]
    if a == 2:
        pos = [pos[0], pos[1] - 1]
    if a == 3:
        pos = [pos[0] + 1, pos[1]]
    if a == 4:
        pos = [pos[0] - 1, pos[1]]
    for i in range(0, len(dangers), 2):
        if pos[0] == dangers[i]:
            if i + 1 < len(dangers):
                if pos[1] == dangers[i + 1]:
                    opp = random.randint(1, 10)
                    opph = random.randint(1, 30)
                    while True:
                        health -= opp
                        opph -= damage
                        if health <= 0:
                            print("You died")
                            SyntaxError("you have died...")
                        if opph <= 0:
                            print("They died")
                            damage += 3
                            health += 5
                            break
    if pos == [0, 0] or pos == [0, 9] or pos == [9, 0] or pos == [9, 9]:
        v += 1
    if v == 4:
        print("you win")
        exit()
    if health<0:
        SyntaxError("you died")