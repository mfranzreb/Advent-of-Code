
with open("input.txt", "r") as f:
    content = [line.strip("\n").split(" ") for line in f.readlines()]
    i = 0
    for line in content:
        j = 0
        for num in line:
            if num == "A" or num == "X":
                content[i][j] = 1
            if num == "B" or num == "Y":
                content[i][j] = 2
            if num == "C" or num == "Z":
                content[i][j] = 3
            j+=1
        i += 1

    score = 0
    for round in content:
        score += round[1]

        if round[1]-1 == round[0] or round[1]-1 == round[0] -3:
            score += 6
        elif round[0] == round[1]:
            score += 3
    print(score)

    #part 2__________________________
    score = 0
    for round in content:

        if round[1] == 2:
            score += 3
            score += round[0]

        elif round[1] == 3:
            score += 6
            if round[0] ==3:
                score += 1
            else:
                score += round[0] + 1
        else:
            if round[0] == 1:
                score += 3
            else:
                score += round[0] - 1

    print(score)
    f.close()


