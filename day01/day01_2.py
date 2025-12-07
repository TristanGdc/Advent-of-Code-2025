with open("Advent-of-Code-2025/inputs/input01") as f:
    lines = f.readlines()
    dial = 50
    res = 0

    for line in lines:
        dir = 1 if line[0] == 'R' else -1
        action = int(line[1:]) * dir
        rotations = 0
        started_on_zero = dial == 0

        dial += action

        rotations = dial//100
        dial -= rotations * 100

        if dir == -1:
            if started_on_zero:
                rotations +=1
            if dial == 0:
                res +=1

        res += abs(rotations)

    print(res)
