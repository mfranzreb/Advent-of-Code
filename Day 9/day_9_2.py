with open("C:/Users/Marco/Desktop/Advent of Code/Day 9/input.txt") as f:
    content = [line.strip("\n").split(" ") for line in f.readlines()]

    knot_coords = [[0, 0], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)]] 

    for line in content:
        direction = line[0]
        moves = int(line[1])
        i = 0
        while i<moves:
            if direction == "R":
                knot_coords[0][0] = knot_coords[0][0] + 1 
            elif direction == "L":
                knot_coords[0][0] = knot_coords[0][0] - 1 
            elif direction == "U":
                knot_coords[0][1] = knot_coords[0][1] + 1
            elif direction == "D":
                knot_coords[0][1] = knot_coords[0][1] - 1

            j = 1
            while j < len(knot_coords):
                knot = knot_coords[j]

                if j == 1:
                    prev_knot = knot_coords[0]
                else:
                    prev_knot = knot_coords[j-1][-1]

                dist_coords = [prev_knot[0]-knot[-1][0], prev_knot[1]-knot[-1][1]]
                dist = dist_coords[0]**2 + dist_coords[1]**2
                if dist < 2.25:
                    break

                elif prev_knot[0] == knot[-1][0]:
                    if prev_knot[1] - knot[-1][1] > 0:
                        knot.append((knot[-1][0], knot[-1][1] + 1))
                    else:
                        knot.append((knot[-1][0], knot[-1][1] - 1))

                elif prev_knot[1] == knot[-1][1]:
                    if prev_knot[0] - knot[-1][0] > 0:
                        knot.append((knot[-1][0] + 1, knot[-1][1]))
                    else:
                        knot.append((knot[-1][0] - 1, knot[-1][1]))

                elif abs(prev_knot[0]-knot[-1][0]) == 1:
                    if prev_knot[1] - knot[-1][1] > 0:
                        knot.append((prev_knot[0], knot[-1][1] + 1))
                    else:
                        knot.append((prev_knot[0], knot[-1][1] - 1))

                elif abs(prev_knot[1]-knot[-1][1]) == 1:
                    if prev_knot[0] - knot[-1][0] > 0:
                        knot.append((knot[-1][0] + 1, prev_knot[1]))
                    else:
                        knot.append((knot[-1][0] - 1, prev_knot[1]))
                else:
                    knot.append(knot_coords[j-1][-2])

                j += 1

            i += 1
        
    positions_visited = set(knot_coords[-1])
    print(len(positions_visited)) 
    f.close()

    
