import matplotlib.pyplot as plt

def findMeanTimeIS():
    data = []
    with open("stat.txt", 'r') as f:
        for line in f:
            data.append(line)
    f.close()
    # return data[6]
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    for i in range(5, len(data), 8):
        newData = data[i].split(" ")
        newData = [float(i) for i in newData]
        temp1.append(newData[0])
        temp2.append(newData[1])
        temp3.append(newData[2])
        temp4.append(newData[3])
        temp5.append(newData[4])
    mean1 = sum(temp1)/len(temp1)
    mean2 = sum(temp2)/len(temp2)
    mean3 = sum(temp3)/len(temp3)
    mean4 = sum(temp4)/len(temp4)
    mean5 = sum(temp5)/len(temp5)
    return mean1, mean2, mean3, mean4, mean5

def findMeanTimeJ():
    data = []
    with open("stat.txt", 'r') as f:
        for line in f:
            data.append(line)
    f.close()
    # return data[6]
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    for i in range(7, len(data), 8):
        newData = data[i].split(" ")
        newData = [float(i) for i in newData]
        temp1.append(newData[0])
        temp2.append(newData[1])
        temp3.append(newData[2])
        temp4.append(newData[3])
        temp5.append(newData[4])
    mean1 = sum(temp1)/len(temp1)
    mean2 = sum(temp2)/len(temp2)
    mean3 = sum(temp3)/len(temp3)
    mean4 = sum(temp4)/len(temp4)
    mean5 = sum(temp5)/len(temp5)
    return mean1, mean2, mean3, mean4, mean5

def findMeanTimeRandomIS():
    data = []
    with open("statRandom.txt", 'r') as f:
        for line in f:
            data.append(line)
    f.close()
    # return data[6]
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    for i in range(5, len(data), 8):
        newData = data[i].split(" ")
        newData = [float(i) for i in newData]
        temp1.append(newData[0])
        temp2.append(newData[1])
        temp3.append(newData[2])
        temp4.append(newData[3])
        temp5.append(newData[4])
    mean1 = sum(temp1)/len(temp1)
    mean2 = sum(temp2)/len(temp2)
    mean3 = sum(temp3)/len(temp3)
    mean4 = sum(temp4)/len(temp4)
    mean5 = sum(temp5)/len(temp5)
    return mean1, mean2, mean3, mean4, mean5

def findMeanTimeRandomJ():
    data = []
    with open("statRandom.txt", 'r') as f:
        for line in f:
            data.append(line)
    f.close()
    # return data[6]
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    for i in range(7, len(data), 8):
        newData = data[i].split(" ")
        newData = [float(i) for i in newData]
        temp1.append(newData[0])
        temp2.append(newData[1])
        temp3.append(newData[2])
        temp4.append(newData[3])
        temp5.append(newData[4])
    mean1 = sum(temp1)/len(temp1)
    mean2 = sum(temp2)/len(temp2)
    mean3 = sum(temp3)/len(temp3)
    mean4 = sum(temp4)/len(temp4)
    mean5 = sum(temp5)/len(temp5)
    return mean1, mean2, mean3, mean4, mean5

def findMeanTimeB():
    data = []
    with open("statsBinary.txt", 'r') as f:
        for line in f:
            data.append(line)
    f.close()
    # return data[6]
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    for i in range(5, len(data), 6):
        newData = data[i].split(" ")
        newData = [float(i) for i in newData]
        temp1.append(newData[0])
        temp2.append(newData[1])
        temp3.append(newData[2])
        temp4.append(newData[3])
        temp5.append(newData[4])
    mean1 = sum(temp1)/len(temp1)
    mean2 = sum(temp2)/len(temp2)
    mean3 = sum(temp3)/len(temp3)
    mean4 = sum(temp4)/len(temp4)
    mean5 = sum(temp5)/len(temp5)
    return mean1, mean2, mean3, mean4, mean5

def findMeanTimeRandomB():
    data = []
    with open("statsBinaryRandom.txt", 'r') as f:
        for line in f:
            data.append(line)
    f.close()
    # return data[6]
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    temp5 = []
    for i in range(5, len(data), 6):
        newData = data[i].split(" ")
        newData = [float(i) for i in newData]
        temp1.append(newData[0])
        temp2.append(newData[1])
        temp3.append(newData[2])
        temp4.append(newData[3])
        temp5.append(newData[4])
    mean1 = sum(temp1)/len(temp1)
    mean2 = sum(temp2)/len(temp2)
    mean3 = sum(temp3)/len(temp3)
    mean4 = sum(temp4)/len(temp4)
    mean5 = sum(temp5)/len(temp5)
    return mean1, mean2, mean3, mean4, mean5
timeComplexityIS = findMeanTimeIS()
timeComplexityJ = findMeanTimeJ()
timeComplexityB = findMeanTimeB()
timeComplexityRandomIS = findMeanTimeRandomIS()
timeComplexityRandomJ = findMeanTimeRandomJ()
timeComplexityRandomB = findMeanTimeRandomB()
size = [2000000, 4000000, 6000000, 8000000, 10000000]
def drawGraph(timeIS, timeJ, timeB, size):
# Sample data for three lines
          
    fig, ax = plt.subplots()
    # Plot the three lines
    ax.plot(size, timeIS, label='IS')
    ax.plot(size, timeJ, label='J')
    ax.plot(size, timeB, label='B')
    # ax.plot(size, timeT, label='T')
    # Add a legend to the plot
    plt.legend()

    # Add labels to the x and y axes
    plt.xlabel('Input size')
    plt.ylabel('Time complexity(seconds)')

    # Set the title of the plot
    plt.title('Relation between input size and time complexity  ')

    # Display the plot
    plt.show()
drawGraph(timeComplexityIS, timeComplexityJ, timeComplexityB, size)
# drawGraph(timeComplexityRandomIS, timeComplexityRandomJ, timeComplexityRandomB, size)
