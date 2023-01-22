from timeit import default_timer as timer

beg = timer()


def readInput(fname):
    with open(fname) as f:
        content = [line.strip("\n").split(" ") for line in f.readlines()]
        map = {}
        unstuck_valves = []
        valves_bin_to_name = dict()
        valves_name_to_bin = dict()
        small_map_bin = {}
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
        for i, valve in enumerate(unstuck_valves):
            bit = 1 << i
            valves_bin_to_name[bit] = valve
            valves_name_to_bin[valve] = bit
            small_map_bin[bit] = [small_map[valve][0], dict()]

        for i, v in enumerate(unstuck_valves):
            dist = findShortestPath(map, "AA", v)
            if dist < min_dist:
                min_dist = dist
            bit = 1 << i
            map_aa[-1][bit] = dist
            for j, other_v in enumerate(unstuck_valves[i + 1 :]):
                dist = findShortestPath(map, v, other_v)
                if dist < min_dist:
                    min_dist = dist
                other_bit = 1 << j + i + 1
                small_map_bin[bit][-1][other_bit] = dist
                small_map_bin[other_bit][-1][bit] = dist
                small_map[v][-1][other_v] = dist
                small_map[other_v][-1][v] = dist
        small_map_bin[0] = map_aa
        for i, valve in enumerate(unstuck_valves):
            bit = 1 << i
            valves_bin_to_name[bit] = valve
            valves_name_to_bin[valve] = bit

    f.close()
    return (
        small_map_bin,
        unstuck_valves,
        min_dist,
        valves_bin_to_name,
        valves_name_to_bin,
    )


def main(map, unstuck_valves):
    paths = []
    starting_path = ["AA", [False for i in range(len(unstuck_valves))], 0, 30]
    paths.append(starting_path)
    # start = set()
    # start.add(64)
    """get_half(0)
    score = max(
        findMaxPressure_DFS("AA", 26, halves)
        + findMaxPressure_DFS("AA", 26, halves ^ all_open)
        for halves in possible_halves
    )"""
    score = max(
        findMaxPressure_DFS(0, 26, i) + findMaxPressure_DFS(0, 26, i ^ all_open)
        for i in range((all_open + 1) // 2)
    )
    print(score)

    print(len(cache))


def findMaxPressure_DFS(
    pos, time, opened
):  # PQ al usar @cache hay menos recursiones pero tarda mas? Pq con el graph de 15 nodes en vez de 45 y menos steps hay mas recursiones?
    global cache
    if (
        pos,
        time,
        opened,
    ) in cache:  # understand how this really works
        return cache[(pos, time, opened)]
    score = 0

    if time < min_dist:
        return 0
    for dir, dist in map[pos][-1].items():
        # bit = 1 << unstuck_valves.index(dir)
        if not opened & dir:
            rem_time = time - dist - 1
            if rem_time > 0:
                score = max(
                    score,
                    findMaxPressure_DFS(dir, rem_time, opened | dir)
                    + (time - dist - 1) * map[dir][0],
                )
    cache[(pos, time, opened)] = score
    return score


def get_half(valves_half=int, i=0):
    global counter
    counter += 1
    if i == 7:
        # other_half = valves_half ^ all_open
        if valves_half in possible_halves:
            return 0
        possible_halves.append(valves_half)
        return 0
    for valve in valves_bin:
        if valve & valves_half or (valve > valves_half and valves_half != 0):
            continue
        j = i
        v = int(valves_half)
        v = valve | v
        get_half(v, j + 1)


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
    map, unstuck_valves, min_dist, valves_bin_to_name, valves_name_to_bin = (
        content[0],
        content[1],
        content[2],
        content[3],
        content[4],
    )
    cache = {}
    counter = 0
    all_open = int("".join(["1" for i in unstuck_valves]), 2)
    possible_halves = []
    valves_bin = valves_bin_to_name.keys()
    main(map, unstuck_valves)

end = timer()
print(end - beg)
