import random

def compareLists(top, bottom):
    if top < bottom:
        return True
    elif top == bottom:
        return None
    else:
        return False

def mergeSort(list):
    if len(list) == 1:
        return list
    
    else:
        top_half = list[:int(len(list)/2)]
        bottom_half = list[int(len(list)/2):]
        sorted_top = mergeSort(top_half)
        sorted_bottom = mergeSort(bottom_half)
        sorted_list = []
        i = 0
        while True:
            if sorted_top == None or not sorted_top:
                sorted_list.extend(sorted_bottom)
                del sorted_bottom
                return sorted_list
            elif sorted_bottom == None or not sorted_bottom:
                sorted_list.extend(sorted_top)
                del sorted_top
                return sorted_list
            order = compareLists(sorted_top[0], sorted_bottom[0])
            if order == False:
                sorted_list.append(sorted_bottom[0])
                del sorted_bottom[0]
            else:
                sorted_list.append(sorted_top[0])
                del sorted_top[0]

            



randomlist = []
for i in range(0,80):
    n = random.randint(1,500)
    randomlist.append(n)
print(randomlist)
sorted = mergeSort(randomlist)
print(sorted)



    
