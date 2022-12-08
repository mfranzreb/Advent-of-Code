with open("input.txt", "r") as f:
    grid_rows = [line.strip("\n") for line in f.readlines()]
    for line in grid_rows:
        grid_rows[grid_rows.index(line)] = [int(x) for x in line]

    
    grid_columns = []
    i = 0
    while i < len(grid_rows[0]):
        column = []
        for line in grid_rows:
            column.append(line[i])

        grid_columns.append(column)
        i+=1

    i = 0
    visible_trees = 0
    while i < len(grid_rows):
        current_row = i
        if current_row == 0 or current_row == len(grid_rows) -1:
            visible_trees += len(grid_rows[0])
            i += 1
            continue
        j = 0
        while j < len(grid_rows[0]):
            current_tree = j
            tree_height = grid_rows[i][j]
            if current_tree == 0 or current_tree == len(grid_rows[0]) -1:
                visible_trees += 1
            else:
                trees_left = grid_rows[i][:current_tree]
                trees_right = grid_rows[i][current_tree+1:]

                if tree_height > max(trees_left) or tree_height > max(trees_right):
                    visible_trees +=1

                else:
                    
                    trees_above = grid_columns[current_tree][:current_row]
                    trees_below = grid_columns[current_tree][current_row+1:]

                    if tree_height > max(trees_above) or tree_height > max(trees_below):
                        visible_trees +=1   
            j += 1
        i += 1

    print(visible_trees)


    #part 2_________

    i = 0
    max_score = 0
    while i < len(grid_rows):
        current_row = i
        j = 0
        while j < len(grid_rows[0]):
            view_score = 0
            current_tree = j
            view_left = 0
            view_right = 0
            view_up = 0
            view_down = 0
            tree_height = grid_rows[current_row][current_tree]

            trees_left = grid_rows[current_row][:current_tree]
            trees_left.reverse()
            trees_right = grid_rows[current_row][current_tree+1:]
            trees_up = grid_columns[current_tree][:current_row]
            trees_up.reverse()
            trees_down = grid_columns[current_tree][current_row+1:]

            for tree in trees_left:
                #print(tree)
                if tree_height >= tree:
                    view_left += 1
                elif len(trees_left)!= 1:
                    view_left = 1
                else:
                    break
                if tree_height == tree:
                    break

            for tree in trees_right:
                if tree_height >= tree:
                    view_right += 1
                elif len(trees_right)!= 1:
                    view_right = 1
                else:
                    break
                if tree_height == tree:
                    break

            for tree in trees_up:
                if tree_height >= tree:
                    view_up += 1
                elif len(trees_up)!= 1:
                    view_up = 1
                else:
                    break
                if tree_height == tree:
                    break

            for tree in trees_down:
                if tree_height >= tree:
                    view_down += 1
                elif len(trees_down)!= 1:
                    view_down = 1
                else:
                    break
                if tree_height == tree:
                    break

            view_score = view_down*view_left*view_up*view_right
            if view_score > max_score:
                max_score = view_score
   
            j += 1
        i += 1
                      

    print(max_score)
    f.close()