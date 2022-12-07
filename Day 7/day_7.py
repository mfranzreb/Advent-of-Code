from timeit import default_timer as timer
start = timer()


with open("input.txt", "r") as f:
    content = [line.strip("\n") for line in f.readlines()]
    content = "_".join(content)
    content = content.split("$ cd ")
    computer = {}
    
    content_part_one = content[2:]
    path = "/"
    for command in content_part_one:

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
                if subkey.startswith(key):
                    new_value += subvalue
            computer_list[i][key] = new_value
            if new_value < 100000:
                total_score += new_value
        i -= 1
    print(total_score)
    #part 2_______________


    
    total_used_space = 0
    level_0 = str(content[1:2])
    ls = level_0.split("_")[2:-1]
    for thing in ls:
        if "dir" not in thing:
            total_used_space += int(thing.split(" ")[0])

    for key, value in computer_list[0].items():
        total_used_space += value

    needed_space = total_used_space - 40000000
    smallest_dir_space = 70000000

    for level in computer_list:
        for key, value in level.items():
            if value < smallest_dir_space and value > needed_space:
                smallest_dir_space = value

    print(smallest_dir_space)
    f.close()

end = timer()
print(end - start)






            


