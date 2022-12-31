from timeit import default_timer as timer
import random

beg = timer()


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


# Driver code to test above
randomlist = []
for i in range(0, 5000):
    n = random.randint(1, 500000)
    randomlist.append(n)
# print(randomlist)
sorted = countingSort(randomlist)
# print(randomlist)

end = timer()
print(end - beg)

# This code is contributed by Mohit Kumra
