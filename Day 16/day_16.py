from timeit import default_timer as timer

beg = timer()


def readInput(fname):
    with open(fname) as f:
        content = [line.strip("\n").split(" ") for line in f.readlines()]
        map = {}
        unstuck_valves = []
        unstuck_valves_bin = dict()
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
        for i, valve in enumerate(unstuck_valves):
            bit = 1 << i
            unstuck_valves_bin[bit] = valve

    f.close()
    return small_map, unstuck_valves, min_dist, unstuck_valves_bin


def main(map, unstuck_valves):
    paths = []
    starting_path = ["AA", [False for i in range(len(unstuck_valves))], 0, 30]
    paths.append(starting_path)

    get_combinations(26, "AA", list())

    for comb in valve_combos:
        findMaxPressure_DFS_3(comb, 26)

    score = 0

    for i, pressure in enumerate(order_pressures):
        for j, ele_pressure in enumerate(order_pressures[i:]):
            if not sum(valve_combos[i]) & sum(valve_combos[j + i]):
                if pressure + ele_pressure > score:
                    score = pressure + ele_pressure
    print(score)

    # print(findMaxPressure_DFS("AA", 30, 0), counter)
    # print(findMaxPressure_DFS_2("AA", 26, "AA", 26, 0), counter)
    # print(findMaxPressure_BFS(map, starting_path))
    # print(len(cache))


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


def findMaxPressure_DFS_2(
    pos_me, time_me, pos_ele, time_ele, opened
):  # PQ al usar @cache hay menos recursiones pero tarda mas? Pq con el graph de 15 nodes en vez de 45 y menos steps hay mas recursiones?
    global counter
    global cache
    global valves
    if (pos_me, time_me, pos_ele, time_ele, opened) in cache:
        return cache[(pos_me, time_me, pos_ele, time_ele, opened)]
    score = 0
    counter += 1
    for i, who in enumerate(
        (
            [pos_me, time_me],
            [pos_ele, time_ele],
        )
    ):
        pos, time = who[0], who[1]
        if time < min_dist:
            return 0
        for dir, dist in map[pos][-1].items():
            bit = 1 << valves.index(dir)
            if not opened & bit:
                rem_time = time - dist - 1
                if rem_time > 0:
                    if i == 0:
                        score = max(
                            score,
                            findMaxPressure_DFS_2(
                                dir,
                                rem_time,
                                pos_ele,
                                time_ele,
                                opened | bit,
                            )
                            + (time - dist - 1) * map[dir][0],
                        )
                    else:
                        score = max(
                            score,
                            findMaxPressure_DFS_2(
                                pos_me,
                                time_me,
                                dir,
                                rem_time,
                                opened | bit,
                            )
                            + (time - dist - 1) * map[dir][0],
                        )
    cache[(pos_me, time_me, pos_ele, time_ele, opened)] = score
    return score


def findMaxPressure_DFS_3(order, time):
    pressure = 0
    time
    global unstuck_valves_bin
    global order_pressures
    for i, valve in enumerate(order):
        dir = unstuck_valves_bin[valve]
        if i == 0:
            time -= map["AA"][-1][dir] + 1
        else:
            time -= map[unstuck_valves_bin[order[i - 1]]][-1][dir] + 1
        pressure += time * map[dir][0]

    order_pressures.append(pressure)


def get_combinations(time, pos, valves_open):
    global valve_combos
    if time < min_dist or sum(valves_open) == all_open:
        valve_combos.append(valves_open)
        return 0
    for dir, dist in map[pos][-1].items():
        bit = 1 << unstuck_valves.index(dir)
        if not sum(valves_open) & bit:
            rem_time = time - dist - 1
            if rem_time > 0:
                new_valves_open = list(valves_open)
                new_valves_open.append(bit)
                valve_combos.append(new_valves_open)
                get_combinations(rem_time, dir, new_valves_open)


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
    map, unstuck_valves, min_dist, unstuck_valves_bin = (
        content[0],
        content[1],
        content[2],
        content[3],
    )
    cache = {}
    counter = 0
    valves = list(map.keys())  # quitalo
    valve_combos = []
    all_open = int("".join(["1" for i in unstuck_valves]), 2)
    order_pressures = []
    main(map, unstuck_valves)

end = timer()
print(end - beg)
