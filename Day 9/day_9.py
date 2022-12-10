with open("C:/Users/Marco/Desktop/Advent of Code/Day 9/input.txt") as f:
    content = [line.strip("\n").split(" ") for line in f.readlines()]

    tail_coords = [(0, 0)]
    head_coords = [0, 0] 

    for line in content:
        direction = line[0]
        moves = int(line[1])
        i = 0
        while i<moves:
            if direction == "R":
                head_coords[0] = head_coords[0] + 1 
            elif direction == "L":
                head_coords[0] = head_coords[0] - 1 
            elif direction == "U":
                head_coords[1] = head_coords[1] + 1
            elif direction == "D":
                head_coords[1] = head_coords[1] - 1

            dist_coords = [head_coords[0]-tail_coords[-1][0], head_coords[1]-tail_coords[-1][1]]
            dist = dist_coords[0]**2 + dist_coords[1]**2
            if dist < 2.25:
                i += 1
                continue

            elif head_coords[0] == tail_coords[-1][0]:
                if direction == "U":
                    tail_coords.append((tail_coords[-1][0], tail_coords[-1][1] + 1))
                elif direction == "D":
                    tail_coords.append((tail_coords[-1][0], tail_coords[-1][1] - 1))

            elif head_coords[1] == tail_coords[-1][1]:
                if direction == "R":
                    tail_coords.append((tail_coords[-1][0] + 1, tail_coords[-1][1]))
                elif direction == "L":
                    tail_coords.append((tail_coords[-1][0] - 1, tail_coords[-1][1]))

            elif abs(head_coords[0]-tail_coords[-1][0]) == 1:
                if direction == "U":
                    tail_coords.append((head_coords[0], tail_coords[-1][1] + 1))
                elif direction == "D":
                    tail_coords.append((head_coords[0], tail_coords[-1][1] - 1))

            else:
                if direction == "R":
                    tail_coords.append((tail_coords[-1][0] + 1, head_coords[1]))
                elif direction == "L":
                    tail_coords.append((tail_coords[-1][0] - 1, head_coords[1]))

            i += 1
    positions_visited = set(tail_coords)
    print(len(positions_visited)) 
    f.close()

    
