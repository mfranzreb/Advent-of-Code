import random
from timeit import default_timer as timer

beg = timer()


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
        top_half = list[: int(len(list) / 2)]
        bottom_half = list[int(len(list) / 2) :]
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


def countingSort(arr, l, r):
    count = [0] * (r - l + 1)
    for num in arr:
        count[num - 1] += 1
    current_index = 0
    for index, amount in enumerate(count):
        i = 0
        while i < amount:
            arr[current_index + i] = index + 1
            i += 1
        current_index += amount


randomlist = []
for i in range(0, 5000):
    n = random.randint(1, 50000)
    randomlist.append(n)
# print(randomlist)
# countingSort(randomlist, 1, 50000)
sorted(randomlist)
# print(sorted)

end = timer()
print(end - beg)
