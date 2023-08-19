

def getRow(rowIndex):
    row = [1]

    for i in range(rowIndex):
        temp = row
        middle = []
        row = []
        for j in range(len(temp) - 1):
            middle.append(temp[j] + temp[j+1])
            
        row = [1] + middle + [1]

    return row



print(getRow(0))
print(getRow(1))
print(getRow(3))