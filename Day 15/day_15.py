def read_input(fname):

    with open(fname) as f:
        content = [line for line in f.readlines()]
        coords = []
        max_x, max_y = 0, 0
        min_x, min_y = float("inf"), float("inf")
        for line in content:
            start = 0
            end = 0
            line_coords = []
            j = 0
            for i, text in enumerate(line):
                if text == "=":
                    start = i + 1 - j
                elif text == "," or text == ":" or text == "\n":
                    end = i - j
                    num = int(line[start:end])
                    line_coords.append(num)
                    if num < min_x and len(line_coords) % 2 != 0:
                        min_x = num
                    elif num < min_y and len(line_coords) % 2 == 0:
                        min_y = num
                    elif num > max_x and len(line_coords) % 2 != 0:
                        max_x = num
                    elif num > max_y and len(line_coords) % 2 == 0:
                        max_y = num
                    line = line[end:]
                    j = i

            coords.append(line_coords)
        for coord in coords:
            min_dist = getDist(coord[:2], coord[2:])
            coords[coords.index(coord)].append(min_dist)
            if coord[0] - min_dist < min_x:
                min_x = coord[0] - min_dist
            elif coord[0] + min_dist > max_x:
                max_x = coord[0] + min_dist

    f.close()
    return list([coords, min_x, max_x])


def getDist(coords_one, coords_two):
    return abs(coords_one[0] - coords_two[0]) + abs(coords_one[1] - coords_two[1])


def q1(content, current_y):
    coords, min_x, max_x = content[0], content[1], content[2]

    no_beacon = 0
    for num in range(min_x, max_x + 1):
        is_beacon = False
        for coord in coords:
            min_dist = coord[-1]
            searched_coord = [num, current_y]
            for coord_y in coords:
                if searched_coord == coord_y[2:-1]:
                    is_beacon = True
                    break
            if is_beacon:
                break

            dist = getDist(coord[:2], searched_coord)
            if dist <= min_dist:
                no_beacon += 1
                break

    print(no_beacon)


def q2(content, lower_bound, upper_bound):

    coords = content[0]
    quadrants = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
    beacon_found = False
    for coord in coords:
        for i in range(coord[-1] + 1):
            for a in quadrants:
                search_coord = [
                    coord[0] + (coord[-1] + 1 - i) * a[0],
                    coord[1] + i * a[1],
                ]
                if any(
                    (coord > upper_bound or coord < lower_bound)
                    for coord in search_coord
                ):
                    break
                for other_coord in coords:
                    if getDist(other_coord[:2], search_coord) <= other_coord[-1]:
                        beacon_found = False
                        break
                    beacon_found = True
                if beacon_found:
                    return search_coord[0] * 4000000 + search_coord[1]


if __name__ == "__main__":
    content = read_input("C:/Users/Marco/Desktop/Advent of Code/Day 15/input.txt")
    # q1(content, 10)
    print(q2(content, 0, 4000000))
