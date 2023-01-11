from timeit import default_timer as timer

beg = timer()


class Path:
    def __init__(self, path, closed_valves, pressure, mins_left):
        self.path = path
        self.closed_valves = closed_valves
        self.pressure = pressure
        self.mins_left = mins_left
        self.current_state = (
            self.path[-1],
            set(self.closed_valves),
            self.pressure,
            self.mins_left,
        )

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
        unstuck_valves = []
        small_map = {}
        for i, line in enumerate(content):
            flow_rate = int(line[4][5:-1])
            tunnels = []
            for text in reversed(line):
                if all(char.isupper() for char in text.strip(",")):
                    tunnels.append(text.strip(","))
                else:
                    break
            map[line[1]] = [
                flow_rate,
                tunnels,
            ]

            if flow_rate > 0:
                unstuck_valves.append(line[1])
                small_map[line[1]] = [flow_rate, i, dict()]
        map_aa = [0, dict()]
        for i, v in enumerate(unstuck_valves):
            dist = findShortestPath(map, "AA", v)
            map_aa[-1][v] = dist
            for other_v in unstuck_valves[i:]:
                dist = findShortestPath(map, v, other_v)
                small_map[v][-1][other_v] = dist
                small_map[other_v][-1][v] = dist
        small_map["AA"] = map_aa

    f.close()
    return small_map, unstuck_valves


def main(content):
    map, unstuck_valves = content[0], content[1]
    paths = []
    starting_path = ["AA", [False for i in range(len(unstuck_valves))], 0, 30]
    paths.append(starting_path)

    print(findMaxPressure(map, paths))


def findMaxPressure(map, paths):  # prueba a usar otros algoritmos
    cache = []
    steps = len(paths[0][1])
    buffer = 750  # max flow rate *30 mins
    valves = list(map.keys())
    for min in range(steps):
        new_paths = []
        j = 0
        for i, path in enumerate(paths):  # algo sucio?
            is_smaller = False
            valve, closed_valves, pressure, mins_left = (
                path[0],
                path[1],
                path[2],
                path[3],
            )
            current_state = path[:3]

            if mins_left <= 0:
                continue

            # if current_state[:2] in cache:
            # continue
            j += 1
            # cache.append(current_state)
            for other_path in paths[i:]:
                if current_state[:2] == other_path[:2]:

                    if current_state[-1] > other_path[-2]:
                        paths.remove(other_path)
                    elif current_state[-1] < other_path[-2]:
                        is_smaller = True
                        break
            if is_smaller:
                continue
            for dir, dist in map[valve][-1].items():

                if closed_valves[valves.index(dir)]:
                    continue
                new_mins_left = mins_left - dist - 1
                if new_mins_left < 0:
                    continue
                new_closed_valves = list(closed_valves)
                new_closed_valves[valves.index(dir)] = True
                new_pressure = pressure + map[dir][0] * new_mins_left
                new_path = [dir, new_closed_valves, new_pressure, new_mins_left]
                new_state = new_path[:2]
                # if new_state not in cache:
                new_paths.append(new_path)

        print(j, len(paths))
        if len(new_paths) != 0:
            paths = new_paths
        else:
            break

    max_pressure = 0
    for path in paths:
        if path[2] > max_pressure:
            max_pressure = path[2]

    return max_pressure


def findShortestPath(map, valve_one, valve_two):
    mins = 0
    current_valves = set()
    current_valves.add(valve_one)
    while True:
        new_valves = set()
        for v in current_valves:
            for dir in map[v][-1]:
                new_valves.add(dir)
                if dir == valve_two:
                    mins += 1
                    return mins
        mins += 1
        current_valves = new_valves


if __name__ == "__main__":
    content = readInput("C:/Users/Marco/Desktop/Advent of Code/Day 16/input.txt")
    main(content)

end = timer()
print(end - beg)
