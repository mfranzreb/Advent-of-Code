with open("input.txt", "r") as f:
    content = [line.strip("\n") for line in f.readlines()]
    i = 0
    stacks = [[] for _ in range(9)]
    while i < 8:

        for char in content[i]:
            if (content[i].index(char) + 1) % 2 == 0 and (content[i].index(char) + 1) % 4 !=0:
                chosen_stack = int((content[i].index(char) - 1) / 4)
                content[i] = content[i].replace(char, "0", 1)
                stacks[chosen_stack].append(char)
                
        i+=1
    commands = [int(num) for line in content[10:] for num in line.split(" ") if num.isdigit()]
    print(stacks)
    for stack in stacks:
        stack.reverse()
    print(stacks)
    for i in range(0,len(commands)-1,3):
        j = 0
        while j < commands[i]:
            crate = stacks[commands[i+1] - 1].pop()
            stacks[commands[i+2] - 1].append(crate)
            #print(crate, commands[i], stacks[commands[i+1] - 1], stacks[commands[i+2] - 1])
            j += 1
    crates = [stack[-1] for stack in stacks]
    print(crates)


     