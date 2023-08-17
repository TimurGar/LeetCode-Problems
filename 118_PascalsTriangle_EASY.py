
def generate(numRows):
    triangle = [[1]]
    
    for i in range(numRows - 1):
        temp = triangle[-1]
        middle = []
        newRow = []
        for j in range(len(temp) - 1):
            middle.append(temp[j] + temp[j+1])
            
        newRow = [1] + middle + [1]
        triangle.append(newRow)

    return triangle

print(generate(1))
print(generate(2))
print(generate(3))
print(generate(4))
print(generate(10))