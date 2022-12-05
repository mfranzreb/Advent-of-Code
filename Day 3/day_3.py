with open("input.txt", "r") as f:
    content = [line.strip("\n") for line in f.readlines()]
    repeat_items= []
    score = 0
    for sack in content:
        half = int(len(sack)/2)
        comp_one = set(sack[:half])
        comp_two = set(sack[half:])
        repeat_items.append(list(comp_one.intersection(comp_two))[0])

    for item in repeat_items:
        if item.isupper():
            score = score + int(ord(item)) - 38

        else:
            score = score + int(ord(item)) - 96

    print(score)

