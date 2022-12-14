
def compareLists(list_top, list_bottom):
    if isinstance(list_top, int) and isinstance(list_bottom, int):
        if list_top > list_bottom:
            return False

        elif list_top < list_bottom:
            return True
        else:
            return None

    elif isinstance(list_top, int) or isinstance(list_bottom, int):
        if not list_bottom and isinstance(list_bottom, list):
            return False
        elif not list_top and isinstance(list_top, list):
            return True

        if isinstance(list_top, int):
            for i, num in enumerate(list_bottom):
                if i > 0:
                    return True
                order = compareLists(list_top, num)
                if order is not None:
                    return order
            return None
        else:
            for i, num in enumerate(list_top):
                if i > 0:
                    return False
                order = compareLists(num, list_bottom)
                if order is not None:
                    return order
            return None

    elif len(list_top) == 0 and len(list_bottom) != 0:
        return True
    elif len(list_top) != 0 and len(list_bottom) == 0:
        return False

    else:       
        if all(isinstance(t, int) for t in list_top) and all(isinstance(b, int) for b in list_bottom):

            if len(list_bottom) == 1  and len(list_top) > 1:
                for i, num in enumerate(list_top):
                    if i == 1:
                        return False
                    order = compareLists(num, list_bottom[0])
                    if order == False:
                        return False
                    elif order == True:
                        return True

                return None

            else:
                for i, num_top in enumerate(list_top):
                    if i >= len(list_bottom):
                        return False
                    order = compareLists(num_top, list_bottom[i])
                    if order == False:
                        return False
                    elif order == True:
                        return True

                if len(list_top) < len(list_bottom):
                    return True
                
                return None
            
        elif len(list_bottom) == 1 and len(list_top) > 1:
            for i, obj in enumerate(list_top):
                if i >= 1:
                    return False
                order = compareLists(obj, list_bottom[0])
                if order == False:
                    return False
                elif order == True:
                    return True

            return None

        else:
            for i, current_list_top in enumerate(list_top):
                if i >= len(list_bottom):
                    return False
                order = compareLists(current_list_top, list_bottom[i])
                if order == False:
                    return False
                elif order == True:
                    return True

            if len(list_top) < len(list_bottom):
                return True
            
            return None


def readFile(fname):
    with open(fname) as f:
        content = [line.strip("\n").split("\n") for line in f.read().split("\n\n")]
        for i, block in enumerate(content):
            content[i][0] = eval(block[0])
            content[i][1] = eval(block[1])
            
    f.close()
    return content


content = readFile("C:/Users/Marco/Desktop/Advent of Code/Day 13/input.txt")
indexes = []
order = False
for i, block in enumerate(content):
    top = block[0]
    bottom = block[1]
    
    order = compareLists(top, bottom)
    if order or order == None: indexes.append(i+1)

print(indexes, sum(indexes))
