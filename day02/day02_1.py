with open("Advent-of-Code-2025/inputs/input02") as f:
    data = f.readlines()[0]
    spans = data.split(',')

    res = 0

    for span in spans:
        [start, end] = map(lambda x: int(x), span.split('-'))
        for id in map(lambda x: str(x), range(start, end+1)):
            mid = int(len(id)/2)
            if id[:mid] == id[mid:]:
                res += int(id)

    print(res)
