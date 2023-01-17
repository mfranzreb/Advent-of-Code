from timeit import default_timer as timer

beg = timer()


def readInput(fname):
    with open(fname) as f:
        content = [line.strip("\n").split(" ") for line in f.readlines()]
        map = {}
        unstuck_valves = []
        small_map = {}
        min_dist = float("inf")
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
            if dist < min_dist:
                min_dist = dist
            map_aa[-1][v] = dist
            for other_v in unstuck_valves[i + 1 :]:
                dist = findShortestPath(map, v, other_v)
                if dist < min_dist:
                    min_dist = dist
                small_map[v][-1][other_v] = dist
                small_map[other_v][-1][v] = dist
        small_map["AA"] = map_aa

    f.close()
    return small_map, unstuck_valves, min_dist


def main(map, unstuck_valves):
    paths = []
    starting_path = ["AA", [False for i in range(len(unstuck_valves))], 0, 30]
    paths.append(starting_path)

    print(findMaxPressure_DFS("AA", 30, 0), counter)
    # print(findMaxPressure_BFS(map, starting_path))


"""def findMaxPressure_BFS(map, path):
    cache = {}
    valves = list(map.keys())
    valve, closed_valves, pressure, mins_left = (
        path[0],
        path[1],
        path[2],
        path[3],
    )
    if (valve, closed_valves, mins_left) in cache:
        return cache[(valve, closed_valves, mins_left)]
    for dir, dist in map[valve][-1].items():  # algo sucio?

        if mins_left < min_dist:
            return 0

        if closed_valves[valves.index(dir)]:
            continue
        new_mins_left = mins_left - dist - 1
        if new_mins_left < 0:
            continue
        new_closed_valves = list(closed_valves)
        new_closed_valves[valves.index(dir)] = True
        new_pressure = pressure + map[dir][0] * new_mins_left
        new_path = [dir, new_closed_valves, new_pressure, new_mins_left]
        new_paths.append(new_path)

    max_pressure = 0
    for path in paths:
        if path[2] > max_pressure:
            max_pressure = path[2]
    print(loop_one, loop_two)
    return max_pressure"""


def findMaxPressure_DFS(
    pos, time, opened
):  # PQ al usar @cache hay menos recursiones pero tarda mas? Pq con el graph de 15 nodes en vez de 45 y menos steps hay mas recursiones?
    global counter
    global cache
    global valves
    if (pos, time, opened) in cache:
        return cache[(pos, time, opened)]
    score = 0
    counter += 1
    if time < min_dist:
        return 0
    for dir, dist in map[pos][-1].items():
        bit = 1 << valves.index(dir)
        if not opened & bit:
            rem_time = time - dist - 1
            if rem_time > 0:
                score = max(
                    score,
                    findMaxPressure_DFS(dir, rem_time, opened | bit)
                    + (time - dist - 1) * map[dir][0],
                )
    cache[(pos, time, opened)] = score
    return score


def delSmallestPath(path_one, path_two, cache):
    if path_one[-1] > path_two[-1]:
        cache.remove(path_two)
        cache.add(path_one)
        return cache, True


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
    map, unstuck_valves, min_dist = content[0], content[1], content[2]
    cache = {}
    counter = 0
    valves = list(map.keys())
    main(map, unstuck_valves)

end = timer()
print(end - beg)
