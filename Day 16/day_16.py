from timeit import default_timer as timer

beg = timer()


def readInput(fname):
    with open(fname) as f:
        content = [line.strip("\n").split(" ") for line in f.readlines()]
        map = {}
        unstuck_valves = []
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

    f.close()
    return (
        small_map_bin,
        unstuck_valves,
        min_dist,
    )


def main():
    score_1 = findMaxPressure_DFS(0, 30, 0)
    score_2 = max(
        findMaxPressure_DFS(0, 26, i) + findMaxPressure_DFS(0, 26, i ^ all_open)
        for i in range((all_open + 1) // 2)
        if bin(i).count("1") == 7
    )
    print(score_1)
    print(score_2)

    print(len(cache))


def findMaxPressure_DFS(pos, time, opened):
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
    map, unstuck_valves, min_dist = (
        content[0],
        content[1],
        content[2],
    )
    cache = {}
    all_open = int("".join(["1" for i in unstuck_valves]), 2)
    main()

end = timer()
print(end - beg)
