with open("input.txt", "r") as f:
    content = [line.strip("\n").split(",") for line in f.readlines()]

    count = 0
    for line in content:
        first_pair = line[0].split("-")
        second_pair = line[1].split("-")
        if int(first_pair[0]) >= int(second_pair[0]) and int(first_pair[1]) <= int(second_pair[1]) or int(first_pair[0]) <= int(second_pair[0]) and int(first_pair[1]) >= int(second_pair[1]):
            count +=1

    print(count)
#Part 2___________________

    count = 0
    for line in content:
        first_pair = line[0].split("-")
        second_pair = line[1].split("-")
        if not (int(first_pair[1]) < int(second_pair[0]) or int(first_pair[0]) > int(second_pair[1])):
            count += 1
            
        
    print(count)
    f.close()
