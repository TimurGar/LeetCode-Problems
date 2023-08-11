# Solved with TWO-POINTER Technique

# Notes
# Looked online, mine got a time limit exception, 
# so instead two pointer technique was used

def twoSum(numbers, target):
    start_index = 0
    end_index = len(numbers)-1
    sum = 0

    while(start_index < end_index):
        sum = numbers[start_index] + numbers[end_index]
        if(sum == target):
            return [start_index+1, end_index+1]
        
        elif(sum > target):
            end_index -= 1
        
        else:
            start_index += 1
            
    
print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))
print(twoSum([0,0,3,4], 0))
print(twoSum([5,25,75], 100))
print(twoSum([1,2,3,4,4,9,56,90], 8))
