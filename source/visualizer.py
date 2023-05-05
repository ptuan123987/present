import math

from matplotlib import pyplot as plt
def binay_search(arr,target) :
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
        return binay_search(left, target)
    
    return binay_search(right, target)


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    if low > high or target < arr[low] or target > arr[high]:
        return -1 
    
    #select pivot
    pivot_pos = low + int((float(high - low) / (arr[high] - arr[low])) * (target - arr[low]))
    
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

def visualize_binary_search(arr, target):
    fig, ax = plt.subplots()
    ax.set_xlim(0, len(arr)-1)
    ax.set_ylim(0, max(arr)+1)
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        ax.plot([mid, mid], [0, max(arr)], 'g--')
        ax.plot([low, high], [arr[mid], arr[mid]], 'r-')
        ax.plot(mid, arr[mid], 'bo')
        
        if arr[mid] == target:
            ax.plot(mid, arr[mid], 'go', markersize=10)
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
        plt.pause(1)
        
    ax.plot(mid, arr[mid], 'ro', markersize=10)
    plt.pause(1)
    
    return -1

def main() :
    arr = [1,2,3,4,5,6]
    postion = binay_search(arr,4)
    postion1 = interpolation_search(arr,4)
    postion3 = jump_search(arr,4)
    print(postion)
    print(postion1)
    print(postion3)
   
    
main()