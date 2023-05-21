import math
import time
from dataService import readRandomData, readData
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


def interpolation_search(arr, target, low, high):
    # low = 0
    # high = len(arr) - 1
    
    if low > high or target < arr[low] or target > arr[high]:
        return -1 
    
    if arr[low] == arr[high]:
        if arr[low] == target:
            return low
        else:
            return -1
    #select pivot
    pivot_pos = low + int((float(high - low) / (arr[high] - arr[low])) * (target - arr[low]))
    print(pivot_pos)
    
    if arr[pivot_pos] == target:
        return pivot_pos
    
    if arr[pivot_pos] < target:
        return interpolation_search(arr, target, pivot_pos+1, high)
    
    return interpolation_search(arr, target, low, pivot_pos-1)

def jump_search(arr, target, low, high) :
    # low = 0
    # high = len(arr) - 1
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

 
def testIS(input, step):

    inputSize = []
    timeComplexityT = []

    for i in range(len(input)):
        start = time.time()
        newData = input[i].split(" ")
        newData.pop(-1)
        newData = [int(i) for i in newData]
        newData.sort()
        # x = 150000000 * (i + 1)
        length = len(newData)
        x = newData[int(length * step)]
        inputSize.append(length)

        result = interpolation_search(newData, x, 0, length - 1)
        # print(result)
        if result == -1:
            print(f"Element {x} not found in the array.")
        else:
            print(f"Element {x} found at index {result}.")
        end = time.time()
        timeComplexityT.append(end - start)

    for i in range(len(timeComplexityT)):
        print(f"Time passed: {timeComplexityT[i]}")
        print(inputSize[i])
    return timeComplexityT, inputSize, x

def testJ(input, step):
    inputSize = []
    timeComplexityJ = []

    for i in range(len(input)):
        start = time.time()
        newData = input[i].split(" ")
        newData.pop(-1)
        newData = [int(i) for i in newData]
        newData.sort()
        # x = 150000000 * (i + 1)
        length = len(newData)
        x = newData[int(length * step)]
        inputSize.append(length)

        result = interpolation_search(newData, x, 0, length - 1)
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

def testBinary(input, step):
    inputSize = []
    timeComplexityJ = []

    for i in range(len(input)):
        start = time.time()
        newData = input[i].split(" ")
        newData.pop(-1)
        newData = [int(i) for i in newData]
        newData.sort()
        # x = 150000000 * (i + 1)
        length = len(newData)
        x = newData[int(length * step)]
        inputSize.append(length)

        result = binay_search(newData, x)
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
    # input = readRandomData()
    input = readData()
    del input[0]
    tempSize = 200000
    # print(a//19)

    step = []
    for i in range(0, tempSize + 1, tempSize//20):
        step.append(i/tempSize)
    del step[-1]
    for i in step:
        # timeComplexityIS = testIS(input, i)[0]
        # timeComplexityJ, inputSize = testJ(input, i)
        timeComplexityB, inputSize = testBinary(input, i)
        # makeStatistics(timeComplexityIS, timeComplexityJ, inputSize, i * 20)
        # makeStatisticsFromRandomData(timeComplexityIS, timeComplexityJ, inputSize, i * 20)
        # makeStatsBinary(timeComplexityB, inputSize, i * 20)
        makeStatsBinary2(timeComplexityB, inputSize, i * 20)

    # createData()
    # createRandomData()
    
    
    # timeComplexityT = testT(input)[0]
    # drawGraph(timeComplexityIS, timeComplexityJ, inputSize)
    # print(f"Time passed: {end - start}")

def makeStatistics(timeIS, timeJ, size, index):
    with open("stat.txt", 'a') as f:
        timeISArray = [str(elem) for elem in timeIS]
        timeJArray = [str(elem) for elem in timeJ]
        sizeArray = [str(elem) for elem in size]
        f.write(f"\nIndex: {index}\n")
        f.write("Input size:  \n")
        f.write(" ".join(sizeArray))
        f.write("\nTime complexity IS: \n")
        f.write(" ".join(timeISArray))
        f.write("\nTime complexity J: \n")
        f.write(" ".join(timeJArray))
        f.write("\n")
    f.close() 


def makeStatisticsFromRandomData(timeIS, timeJ, size, index):
    with open("statRandom.txt", 'a') as f:
        timeISArray = [str(elem) for elem in timeIS]
        timeJArray = [str(elem) for elem in timeJ]
        sizeArray = [str(elem) for elem in size]
        f.write(f"\nIndex: {index}th\n")
        f.write("Input size:  \n")
        f.write(" ".join(sizeArray))
        f.write("\nTime complexity IS: \n")
        f.write(" ".join(timeISArray))
        f.write("\nTime complexity J: \n")
        f.write(" ".join(timeJArray))
        f.write("\n")
    f.close()
def makeStatsBinary(time, size, index):
    with open("statsBinaryRandom.txt", 'a') as f:
        timeB =  [str(elem) for elem in time]
        sizeArray = [str(elem) for elem in size]
        f.write(f"\nIndex: {index}th\n")
        f.write("Input size:  \n")
        f.write(" ".join(sizeArray))
        f.write("\nTime complexity Binary: \n")
        f.write(" ".join(timeB))
        f.write("\n")
def makeStatsBinary2(time, size, index):
    with open("statsBinary.txt", 'a') as f:
        timeB =  [str(elem) for elem in time]
        sizeArray = [str(elem) for elem in size]
        f.write(f"\nIndex: {index}th\n")
        f.write("Input size:  \n")
        f.write(" ".join(sizeArray))
        f.write("\nTime complexity Binary: \n")
        f.write(" ".join(timeB))
        f.write("\n")



main()



