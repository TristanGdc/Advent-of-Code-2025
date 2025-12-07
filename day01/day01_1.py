with open("Advent-of-Code-2025/inputs/input01") as f:
    lines = f.readlines()
    dial = 50
    res = 0

    for line in lines:
        dir = 1 if line[0] == 'R' else -1
        action = int(line[1:]) * dir

        dial += action
        dial -= dial//100 * 100

        if (dial == 0):
            res+=1

    print(res)
