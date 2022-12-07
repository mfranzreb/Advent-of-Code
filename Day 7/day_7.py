with open("input.txt", "r") as f:
    content = [line.strip("\n") for line in f.readlines()]
    content = "_".join(content)
    content = content.split("$")
    computer = []
    
    content = content[2:]
    path = []
    #print(content)
    for command in content:
        if "cd" in command and not ".." in command:
            current_dir = command.split(" ")[1]
            path.append(current_dir)
            

        if " cd .." in command:
            path.pop()
        if "ls" in command:
            ls = command.split("_")[1:]
            size = 0
            for subthing in ls:
                subdir_there = False
                if "dir" in subthing:
                    subdir_there = True
                    computer[0][]
                else:
                    file = subthing.split(" ")
                    for part in file:
                        if part.isdigit():
                            size += int(part)
            


