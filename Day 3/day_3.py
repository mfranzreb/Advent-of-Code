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

#part 2______________________
    badges = []
    score = 0
    i = 0
    while i < len(content) - 1:
        sack_one = set(content[i])
        sack_two = set(content[i+1])
        sack_three = set(content[i+2])
        badges.append(list(sack_one.intersection(sack_two, sack_three))[0])
        i += 3
        
    for item in badges:
        if item.isupper():
            score = score + int(ord(item)) - 38

        else:
            score = score + int(ord(item)) - 96

    print(score)
    f.close()