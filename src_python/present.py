import math
import random
import time
import matplotlib.pyplot as plt

# pos = low + [(x - arr[low]) * (high - low) / (arr[high] - arr[low])]
# O(log(log(n)))
def binary_search(arr, target) :
    #base case : if arr is empty
    if (len(arr) == 0) :
        return 0
    
    # divide arr into 2 subarr
    middle_pos = len(arr) //2
    left = arr[:middle_pos]
    right = arr[middle_pos + 1:]
    
    if (arr[middle_pos] == target) :
        return middle_pos
    
    if arr[middle_pos] > target :
        return binary_search(left, target)
    
    return binary_search(right, target)


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    if low > high or target < arr[low] or target > arr[high]:
        return -1 
    
    #select pivot
    pivot_pos = low + int((float(high - low) / (arr[high] - arr[low])) * (target - arr[low]))
    print(pivot_pos)
    
    if arr[pivot_pos] == target:
        return pivot_pos
    
    if arr[pivot_pos] < target:
        return interpolation_search(arr, target, pivot_pos+1, high)
    
    return interpolation_search(arr, target, low, pivot_pos-1)

def jump_search(arr, target) :
    low = 0
    high = len(arr) - 1
    if low > high :
        return -1
    step = int(math.sqrt(len(arr)))
    prev = low
    
    # Jumping through the array
    while arr[min(step, high)-1] < target:
        prev = step
        step += int(math.sqrt(high-low))
        if prev >= high:
            return -1
    
    # Linear search within the block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, high):
            return -1
    
    # If element is found, return its index
    if arr[prev] == target:
        return prev
    
    if arr[prev] > target:
        return jump_search(arr, target, low, prev-1)
    
    return jump_search(arr, target, prev+1, high)

def createData():
    for i in range(1, 6):    
        length = 200000000 * i
        data = [i for i in range(0, int(length), 100)]
        # Open file in write mode
        with open("data.txt", "a") as f:
            f.write("\n")
            # Write data to file
            for item in data:
                f.write("%s" % item)
                f.write(" ")

        f.close()

def readData():
    input = []
    with open("data.txt", "r") as f:
        for line in f:
    # Read the contents of the file
            input.append(line)
    return input

def testIS(input):
    inputSize = []
    timeComplexityIS = []

    for i in range(len(input)):
        start = time.time()
        newData = input[i].split(" ")
        newData.pop(-1)
        newData = [int(i) for i in newData]
        x = 150000000 * (i + 1)
        length = len(newData)
        inputSize.append(length)

        result = interpolation_search(newData, x)
        # print(result)
        if result == -1:
            print(f"Element {x} not found in the array.")
        else:
            print(f"Element {x} found at index {result}.")
        end = time.time()
        timeComplexityIS.append(end - start)

    for i in range(len(timeComplexityIS)):
        print(f"Time passed: {timeComplexityIS[i]}")
        print(inputSize[i])
    return timeComplexityIS, inputSize

def testJ(input):
    inputSize = []
    timeComplexityJ = []

    for i in range(len(input)):
        start = time.time()
        newData = input[i].split(" ")
        newData.pop(-1)
        newData = [int(i) for i in newData]
        x = 150000000 * (i + 1)
        length = len(newData)
        inputSize.append(length)

        result = interpolation_search(newData, x)
        # print(result)
        if result == -1:
            print(f"Element {x} not found in the array.")
        else:
            print(f"Element {x} found at index {result}.")
        end = time.time()
        timeComplexityJ.append(end - start)

    for i in range(len(timeComplexityJ)):
        print(f"Time passed: {timeComplexityJ[i]}")
        print(inputSize[i])
    return timeComplexityJ, inputSize

def main():
    input = readData()
    del input[0]
    
    timeComplexityIS = testIS(input)[0]
    timeComplexityJ, inputSize = testJ(input)[0]
    # createData()
    drawGraph(timeComplexityIS, timeComplexityJ, inputSize)
    # print(f"Time passed: {end - start}")

def drawGraph(timeIS, timeJ, size):
# Sample data for three lines
    fig, ax = plt.subplots()
    # Plot the three lines
    ax.plot(size, timeIS, label='IS')
    ax.plot(size, timeJ, label='J')
    
    # Add a legend to the plot
    plt.legend()

    # Add labels to the x and y axes
    plt.xlabel('Input size')
    plt.ylabel('Time complexity')

    # Set the title of the plot
    plt.title('Relation between input size and time complexity  ')

    # Display the plot
    plt.show()

main()




