def smallestVal(array, smallest=float('inf'), index=0):
    if index == len(array):
        return smallest
    if array[index] < smallest:
        smallest = array[index]
    return smallestVal(array, smallest, index + 1)

print("SMALLEST: " + str(smallestVal([4,7,1,3,7,4,6,3])))