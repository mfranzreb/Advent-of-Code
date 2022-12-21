def isListEmpty(inList):
    if isinstance(inList, list): # Is a list
        return all( map(isListEmpty, inList) )
    return False # Not a list

def compare_lists(list_top, list_bottom):
    if isinstance(list_top, int) and isinstance(list_bottom, int):
        if list_top > list_bottom:
            return False

        elif list_top < list_bottom:
            return True
        else:
            return None

    elif isinstance(list_top, int) or isinstance(list_bottom, int):
        if isinstance(list_top, int):
            for num in list_bottom:
                order = compare_lists(list_top, num)
                if order == False:
                    return False

    elif len(list_top) == 0 and len(list_bottom) != 0:
        return True
    elif len(list_top) != 0 and len(list_bottom) == 0:
        return False

    else:       
        if all(isinstance(t, int) for t in list_top) and all(isinstance(b, int) for b in list_bottom):

            if len(list_top) > len(list_bottom) and len(list_bottom) > 1:
                return False

            elif len(list_bottom) == 1  and len(list_top) > 1:
                for num in list_top:
                    order = compare_lists(num, list_bottom[0])
                    if order == False:
                        return False
                    elif order == True:
                        return True

                return None

            else:
                for i, num_top in enumerate(list_top):
                    order = compare_lists(num_top, list_bottom[i])
                    if order == False:
                        return False
                    elif order == True:
                        return True

                if len(list_top) < len(list_bottom):
                    return True
                
                return None
            
        elif len(list_top) > len(list_bottom) and len(list_bottom) > 1:
                return False

        elif len(list_bottom) == 1 and len(list_top) > 1:
            for obj in list_top:
                order = compare_lists(obj, list_bottom)
                if order == False:
                    return False
                elif order == True:
                    return True

            return None

        else:
            for i, current_list_top in enumerate(list_top):
                order = compare_lists(current_list_top, list_bottom[i])
                if order == False:
                    return False
                elif order == True:
                    return True

            if len(list_top) < len(list_bottom):
                return True
            
            return None





with open("C:/Users/Marco/Desktop/Advent of Code/Day 13/test.txt") as f:
    content = [line.strip("\n").split("\n") for line in f.read().split("\n\n")]
    for i, block in enumerate(content):
        content[i][0] = eval(block[0])
        content[i][1] = eval(block[1])
    
    indexes = []
    order = False
    for i, block in enumerate(content):
        top = block[0]
        bottom = block[1]
        order = compare_lists(top, bottom)
        if order or order == None: indexes.append(i+1)

    print(indexes, sum(indexes))
    f.close()