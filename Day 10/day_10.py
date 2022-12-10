with open("C:/Users/Marco/Desktop/Advent of Code/Day 10/input.txt") as f:
    content = [line.strip("\n") for line in f.readlines()]

    cycle_during = 0 #cycle that i am in
    register = 1

    signal_strengths = []

    register_per_cycle = {}

    for i, line in enumerate(content):
        if "noop" in line:
            cycle_during += 1
            register_per_cycle[cycle_during] = register
        else:
            cycle_during += 2
            register_per_cycle[cycle_during - 1] = register
            register_per_cycle[cycle_during] = register
            register += int(line.split(" ")[1])

    signal_strengths = 0
    for i in range(20, 221, 40):
        signal_strengths += i*register_per_cycle[i]
    
    print(signal_strengths)
    #part 2____________

    pixels = []
    screen_lines = [40, 80, 120, 160, 200, 240]
    reset_line = 0
    current_line = 0
    line_pixels = ""
    for key, value in register_per_cycle.items():
        pixel_pos = key - 1 - reset_line
        if pixel_pos + 1 == value or pixel_pos - 1 == value or pixel_pos == value:
            line_pixels += "#"
        else:
            line_pixels += "."

        if key in screen_lines:
            reset_line = key
            pixels.append(line_pixels)
            line_pixels = ""

    screen = "\n".join(pixels)

    print(screen)

    f.close()
    
