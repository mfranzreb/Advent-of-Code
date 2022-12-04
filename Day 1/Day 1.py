with open("input.txt", "r") as f:
    content = [line.split("\n")[0] for line in f.readlines()]
    calories = 0
    info = []

    for num in content:
        if not num:
            info.append(calories)
            calories = 0
        else:
            calories += int(num)
    info.sort(reverse=True)

    f.close()

print("Max calories on one elf: ", info[0])
print("Calories on top three elves: ", sum(info[:3]))



