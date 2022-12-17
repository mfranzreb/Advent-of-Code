from copy import copy
from timeit import default_timer as timer

beg = timer()


def read_input():

    with open("C:/Users/Marco/Desktop/Advent of Code/Day 12/input.txt") as f:
        content = [[line.strip("\n")] for line in f.readlines()]
        for i, line in enumerate(content):
            for text in line:
                content[i] = [ord(char) - 96 for char in text]

    f.close()
    return content


def main():
    graph = read_input()
    coords = get_coords(graph)
    start_coord, end_coord = coords[0], coords[1]
    graph[end_coord[1]][end_coord[0]] = ord("z") - 96
    graph[start_coord[1]][start_coord[0]] = ord("a") - 96

    

    path = shortest_path(graph, start_coord, end_coord)

    #print(path)
    print(len(path) - 1)


def shortest_path(graph, start_coord, end_coord):
    paths = [[start_coord]]
    #i = 1
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while True:
        new_paths = []
        for path in paths:
            current_coord = path[-1]
            new_steps = get_possible_directions(directions, paths, new_paths, graph, current_coord)
            for step in new_steps:

                if step == end_coord:
                    new_path = copy(path)
                    new_path.append(step)
                    return new_path

                else:
                    new_path = copy(path)
                    new_path.append(step)
                    new_paths.append(new_path)
        """if i % 5== 0 and i > 322:
            vis_map = [["_" for i in range(map_width+1)] for j in range(map_height+1)] # visualization
            for path in paths:
                for coord in path:
                    vis_map[coord[1]][coord[0]] = "0"
            for g, line in enumerate(vis_map):
                s = ""
                for char in line:
                    
                    s +=char
                vis_map[g] = s

            txt =  "\n".join(vis_map)
            print(txt)
            print("\n")"""
        if new_paths:
            paths.clear()
            paths.append(new_paths)
            paths = paths[0]
        #i+=1  

def get_possible_directions(directions, paths, new_paths, graph, current_coord):
    map_width = len(graph[0]) -1 
    map_height = len(graph) -1
    new_steps = []
    for dir in directions:
        new_step = [current_coord[0] + dir[0], current_coord[1] + dir[1]]
        if not (any(new_step in p for p in paths) or any(new_step in t for t in new_paths)) and not (new_step[0] < 0 or new_step[0] > map_width) and not (new_step[1] < 0 or new_step[1] > map_height) and graph[new_step[1]][new_step[0]] - 1 <= graph[current_coord[1]][current_coord[0]]:
            new_steps.append(new_step)

    return new_steps



                
def get_coords(graph):
    for y, line in enumerate(graph):
        for x, num in enumerate(line):
            if num == -13:
                start_coord = [x, y]
            elif num == -27:
                end_coord = [x, y]

    return start_coord, end_coord
        



if __name__ == "__main__":
    main()

end = timer()
print(end - beg)
