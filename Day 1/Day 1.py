with open("input.txt", "r") as f:
    content = [line.split("\n")[0] for line in f.readlines()]
    calories = 0
    info = {}
    i = 1
    max_calories = 0
    for num in content:
        
        if not num:
            print("____________________")
            info[i] = calories
            if calories > max_calories:
                max_calories = calories
                max_calories_index = i
            calories = 0
            i+=1
        else:
            calories += int(num)
            print(int(num), calories)

    print("Elf {index} is carrying the most calories, which are {cals}".format(index = max_calories_index, cals = max_calories))


