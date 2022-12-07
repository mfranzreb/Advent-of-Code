with open("input.txt", "r") as f:
    content = [line.strip("\n") for line in f.readlines()]
    content = "_".join(content)
    content = content.split("$ cd ")
    computer = {}
    
    content = content[2:]
    path = "/"
    #print(content)
    for command in content:

        if ".." in command:
            path = path.split("/")[:-1]
            if len(path) ==1:
                path = "/"
            else:
                path ="/".join(path)

        else:
            current_dir = command.split("_")[0]
            if path.endswith("/"):
                path = path + current_dir
            else:
                path = path + "/" + current_dir
            if "ls" in command:
                ls = command.split("_")[2:]
                #print(ls)
                size = 0
                for subthing in ls:
                    if "dir" in subthing:
                        continue
                    else:
                        file = subthing.split(" ")
                        for part in file:
                            if part.isdigit():
                                size += int(part)
                current_level = len(path.split("/")) - 1

                try:
                    computer["level_{0}".format(current_level)][path] = size
                except KeyError:
                    computer["level_{0}".format(current_level)] = {}
                    computer["level_{0}".format(current_level)][path] = size

    #print(computer)
    computer_list = []
    total_score = 0
    for key, value in computer.items():
        computer_list.append(value)

    for key, value in computer_list[-1].items():
        if value < 100000:
            total_score += value

    i = 7
    
    while i > -1:
        for key, value in computer_list[i].items():
            new_value = value
            for subkey, subvalue in computer_list[i+1].items():
                if key in subkey:
                    new_value += subvalue
            computer_list[i][key] = new_value
            if new_value < 100000:
                total_score += new_value

        i -= 1
    print(total_score)
    #total_computer_space = 




            


