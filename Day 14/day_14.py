def fillSand(cave, pour_x, min_x, max_x, max_y=None):
    sand_units = 0
    while True:
        sand_unit_coord = [pour_x - min_x, 0]
        while True:
            if sand_unit_coord[1] == len(cave) - 1:
                return sand_units

            elif cave[sand_unit_coord[1] + 1][sand_unit_coord[0]] == ".":
                sand_unit_coord = [sand_unit_coord[0], sand_unit_coord[1] + 1]
            elif (
                sand_unit_coord[0] > 0
                and cave[sand_unit_coord[1] + 1][sand_unit_coord[0] - 1] == "."
            ):
                sand_unit_coord = [sand_unit_coord[0] - 1, sand_unit_coord[1] + 1]
            elif (
                sand_unit_coord[0] < max_x - min_x
                and cave[sand_unit_coord[1] + 1][sand_unit_coord[0] + 1] == "."
            ):
                sand_unit_coord = [sand_unit_coord[0] + 1, sand_unit_coord[1] + 1]
            elif sand_unit_coord == [pour_x - min_x, 0]:
                sand_units += 1
                return sand_units
            else:
                cave[sand_unit_coord[1]][sand_unit_coord[0]] = "o"
                sand_units += 1
                if sand_unit_coord[1] == max_y + 1:
                    if sand_unit_coord[0] == max_x - min_x:
                        for i, line in enumerate(cave):
                            if i < max_y + 2:
                                line.append(".")
                                cave[i] = line
                            else:
                                line.append("#")
                                cave[i] = line
                        max_x += 1

                    elif sand_unit_coord[0] == 0:
                        for i, line in enumerate(cave):
                            if i < max_y + 2:
                                line.insert(0, ".")
                                cave[i] = line
                            else:
                                line.insert(0, "#")
                                cave[i] = line
                        min_x -= 1

                break


def readFile(fname):
    with open(fname) as f:
        content = [line.strip("\n").split(" -> ") for line in f.readlines()]
        f.close()
        return content


def makeMapQ1(content):
    max_y, max_x = 0, 0
    min_x = 1000
    for i, line in enumerate(content):
        for j, coord in enumerate(line):
            x, y = int(coord.split(",")[0]), int(coord.split(",")[1])
            content[i][j] = [int(coord.split(",")[0]), int(coord.split(",")[1])]
            if x > max_x:
                max_x = x + 1  # add one column of space to the side
            if y > max_y:
                max_y = y
            if x < min_x:
                min_x = x - 1  # add one column of space to the side

    cave = [["." for i in range(max_x - min_x + 1)] for j in range(max_y + 1)]
    pour_x = 500
    cave[0][pour_x - min_x] = "+"

    for line in content:
        # if content.index(line) != 15:
        # continue
        for j, coord in enumerate(line[:-1]):
            delta_x = line[j + 1][0] - coord[0]
            delta_y = line[j + 1][1] - coord[1]
            y_start = coord[1]
            x_start = coord[0] - min_x
            k = 0
            if delta_x == 0:
                while k <= abs(delta_y):
                    if delta_y > 0:
                        cave[y_start + k][x_start] = "#"
                    else:
                        cave[y_start - k][x_start] = "#"
                    k += 1
            else:
                while k <= abs(delta_x):
                    if delta_x > 0:
                        cave[y_start][x_start + k] = "#"
                    else:
                        cave[y_start][x_start - k] = "#"
                    k += 1

    with open("C:/Users/Marco/Desktop/Advent of Code/Day 14/cave_empty.txt", "w") as fp:
        for item in cave:
            # write each item on a new line
            fp.write("%s\n" % "".join(item))
        fp.close()

    print(fillSand(cave, pour_x, min_x, max_x))

    with open("C:/Users/Marco/Desktop/Advent of Code/Day 14/cave_full.txt", "w") as fp:
        for item in cave:
            # write each item on a new line
            fp.write("%s\n" % "".join(item))
        fp.close()


def makeMapQ2(content):
    max_y, max_x = 0, 0
    min_x = 1000
    for i, line in enumerate(content):
        for j, coord in enumerate(line):
            x, y = int(coord.split(",")[0]), int(coord.split(",")[1])
            content[i][j] = [int(coord.split(",")[0]), int(coord.split(",")[1])]
            if x > max_x:
                max_x = x + 1  # add one column of space to the side
            if y > max_y:
                max_y = y
            if x < min_x:
                min_x = x - 1  # add one column of space to the side

    cave = [
        ["." for i in range(max_x - min_x + 1)] for j in range(max_y + 1 + 2)
    ]  # add 2 for floor
    cave[-1] = ["#" for i in range(max_x - min_x + 1)]
    pour_x = 500
    cave[0][pour_x - min_x] = "+"

    for line in content:
        # if content.index(line) != 15:
        # continue
        for j, coord in enumerate(line[:-1]):
            delta_x = line[j + 1][0] - coord[0]
            delta_y = line[j + 1][1] - coord[1]
            y_start = coord[1]
            x_start = coord[0] - min_x
            k = 0
            if delta_x == 0:
                while k <= abs(delta_y):
                    if delta_y > 0:
                        cave[y_start + k][x_start] = "#"
                    else:
                        cave[y_start - k][x_start] = "#"
                    k += 1
            else:
                while k <= abs(delta_x):
                    if delta_x > 0:
                        cave[y_start][x_start + k] = "#"
                    else:
                        cave[y_start][x_start - k] = "#"
                    k += 1

    with open("C:/Users/Marco/Desktop/Advent of Code/Day 14/cave_empty.txt", "w") as fp:
        for item in cave:
            # write each item on a new line
            fp.write("%s\n" % "".join(item))
        fp.close()

    print(fillSand(cave, pour_x, min_x, max_x, max_y))

    with open("C:/Users/Marco/Desktop/Advent of Code/Day 14/cave_full.txt", "w") as fp:
        for item in cave:
            # write each item on a new line
            fp.write("%s\n" % "".join(item))
        fp.close()


if __name__ == "__main__":
    content = readFile("C:/Users/Marco/Desktop/Advent of Code/Day 14/input.txt")
    makeMapQ2(content)
