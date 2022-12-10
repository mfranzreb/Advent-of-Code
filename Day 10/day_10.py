with open("C:/Users/Marco/Desktop/Advent of Code/Day 10/input.txt") as f:
    content = [line.strip("\n") for line in f.readlines()]

    cycle_during = 1 #cycle that i am in
    register = 1

    signal_strengths = []

    for line in content:
        next_cycle = cycle_during + 1
        if cycle_during % 20 == 0 and (cycle_during - 20)%40 == 0:
            signal_strengths.append(cycle_during*register)
        elif next_cycle % 20 == 0 and (next_cycle - 20)%40 == 0:
            signal_strengths.append(next_cycle*register)


        if "noop" in line:
            cycle_during += 1

        elif "addx" in line:
            cycle_during += 2
            register += int(line.split(" ")[1])

        if cycle_during > 222:
            break
    
    print(sum(signal_strengths))