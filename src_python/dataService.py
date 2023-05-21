import random
def createData():
    for i in range(1, 6):    
        length = 200000000 * i # 200tr
        data = [i for i in range(0, length, 100)]
        
        # Open file in write mode
        with open("data.txt", "a") as f:
            f.write("\n")
            # Write data to file
            for item in data:
                f.write("%s" % item)
                f.write(" ")

        f.close()
def createRandomData():
    for i in range(1, 6):    
        length = 200000000 * i
        data = [random.randint(1, 10000000) for i in range(0, length, 100)]
        
        # Open file in write mode
        with open("randomdata.txt", "a") as f:
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

def readRandomData():
    input = []
    with open("randomdata.txt", "r") as f:
        for line in f:
    # Read the contents of the file
            input.append(line)
    
    return input