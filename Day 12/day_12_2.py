from copy import copy


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
    end_coord = get_end_coord(graph)
    graph[end_coord[1]][end_coord[0]] = ord("z") - 96

    start_coords = get_start_coords(graph, end_coord)

    
    path_lens = []
    for c in start_coords:
        path = shortest_path(graph, c, end_coord)
        path_lens.append(len(path) - 1)

    print(min(path_lens))


def shortest_path(graph, start_coord, end_coord):
    paths = []
    paths.append([start_coord])
    map_width = len(graph[0]) -1 
    map_height = len(graph) -1
    i = 1
    filtering = False
    while True:
        new_paths = []
        for path in paths:
            current_coord = path[-1]
            possible_directions = []
            if len(path) == 1:
                if current_coord[1] == 0:
                    possible_directions.append((1, 0))
                    possible_directions.append((0, 1))
                elif current_coord[1] == 40:
                    possible_directions.append((1, 0))
                    possible_directions.append((0, -1))
                else:
                    possible_directions.append((1, 0))
                    possible_directions.append((0, -1))
                    possible_directions.append((0, 1))

            else:
                if current_coord[0] != 0 and current_coord[0] - 1 != path[-2][0] and (graph[current_coord[1]][current_coord[0] - 1] - 1 <=  graph[current_coord[1]][current_coord[0]]): #Y coordinate goes first!!
                    possible_directions.append((-1, 0))

                if current_coord[0] != map_width and current_coord[0] + 1 != path[-2][0] and graph[current_coord[1]][current_coord[0] + 1] - 1 <=  graph[current_coord[1]][current_coord[0]]:
                    possible_directions.append((1, 0))

                if current_coord[1] != 0 and current_coord[1] - 1 != path[-2][1] and graph[current_coord[1] - 1][current_coord[0]] - 1 <=  graph[current_coord[1]][current_coord[0]]:#en y, sumar uno en indice es ir hacia baajo
                    possible_directions.append((0, -1))

                if current_coord[1] != map_height and current_coord[1] + 1 != path[-2][1] and graph[current_coord[1] + 1][current_coord[0]] - 1 <=  graph[current_coord[1]][current_coord[0]]:
                        possible_directions.append((0, 1))

            for dir in possible_directions:
                new_step = tuple(map(lambda i, j: i + j, current_coord, dir))
                if abs(new_step[0] - end_coord[0]) <= 10:
                    filtering = True
                if new_step == end_coord:
                    new_path = copy(path)
                    new_path.append(new_step)
                    return new_path

                elif any(new_step in p for p in paths) or any(new_step in t for t in new_paths):
                    continue

                else:
                    if filtering and abs(new_step[0] - end_coord[0]) > 10:
                        continue
                    else:
                        new_path = copy(path)
                        new_path.append(new_step)
                        new_paths.append(new_path)
        if i % 5== 0 and i > 500:
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
            print("\n")
        if new_paths:
            paths.clear()
            paths.append(new_paths)
            paths = paths[0]
        i+=1  
                
def get_end_coord(graph):
    for y, line in enumerate(graph):
        for x, num in enumerate(line):
            if num == -27:
                end_coord = (x, y)

    return end_coord

def get_start_coords(graph, end_coords):#easy way
    start_coords = []
    for y in range(len(graph)):
        start_coords.append((0, y))
    return start_coords

            
        



if __name__ == "__main__":
    main()
