class Path:
    def __init__(self, path, closed_valves, pressure):
        self.path = path
        self.closed_valves = closed_valves
        self.pressure = pressure

    def addStep(self, step):
        self.path.append(step)

    def addValve(self, valve):
        self.closed_valves.remove(valve)

    def addPressure(self, pressure, minutes_left):
        self.pressure += pressure * minutes_left


def readInput(fname):
    with open(fname) as f:
        content = [line.strip("\n").split(" ") for line in f.readlines()]
        map = {}
        all_valves = []
        for line in content:
            all_valves.append(line[1])
            tunnels = []
            for text in reversed(line):
                if all(char.isupper() for char in text.strip(",")):
                    tunnels.append(text.strip(","))
                else:
                    break
            map[line[1]] = [
                int(line[4][5:-1]),
                False,
                tunnels,
            ]

    f.close()
    return map, all_valves


def main(content):
    map, all_valves = content[0], content[1]
    paths = []
    starting_path = Path(["AA"], all_valves, 0)
    paths.append(starting_path)
    print(findMaxPressure(map, paths))


def findMaxPressure(map, paths):  # prueba a usar otros algoritmos
    buffer = 750  # max flow rate *30 mins
    for min in range(30, -1, -1):
        new_paths = []
        for i, path_obj in enumerate(paths):  # algo sucio?
            is_smaller = False
            for other_path_obj in paths[i:]:
                if (
                    path_obj.path[-1] == other_path_obj.path[-1]
                    and path_obj != other_path_obj
                    and path_obj.path[-1] in path_obj.closed_valves
                    and other_path_obj.path[-1] in other_path_obj.closed_valves
                    and (
                        all(
                            valve in other_path_obj.closed_valves
                            for valve in path_obj.closed_valves
                        )
                        or all(
                            valve in path_obj.closed_valves
                            for valve in other_path_obj.closed_valves
                        )
                    )
                    or path_obj.pressure < other_path_obj.pressure - buffer
                    or path_obj.pressure > other_path_obj.pressure + buffer
                ):
                    if path_obj.pressure >= other_path_obj.pressure:
                        paths.remove(other_path_obj)
                    else:
                        is_smaller = True
                        break
            if is_smaller:
                continue
            for dir in map[path_obj.path[-1]][-1]:
                if (
                    map[path_obj.path[-1]][0] == 0
                    and len(path_obj.path) > 1
                    and dir == path_obj.path[-2]
                ):
                    continue
                new_path = list(path_obj.path)
                new_path.append(dir)
                new_paths.append(
                    Path(new_path, path_obj.closed_valves, path_obj.pressure)
                )

            if (
                path_obj.path[-1] in path_obj.closed_valves
                and map[path_obj.path[-1]][0] > 0
            ):
                new_closed_valves = list(path_obj.closed_valves)
                new_closed_valves.remove(path_obj.path[-1])
                new_pressure = path_obj.pressure + map[path_obj.path[-1]][0] * (min - 1)
                new_paths.append(Path(path_obj.path, new_closed_valves, new_pressure))

        paths = new_paths

    max_pressure = 0
    for path_obj in paths:
        if path_obj.pressure > max_pressure:
            max_pressure = path_obj.pressure

    return max_pressure


if __name__ == "__main__":
    content = readInput("C:/Users/Marco/Desktop/Advent of Code/Day 16/input.txt")
    print(content)
    main(content)
