# Solved with FAST & SLOW POINTERS Approach

def removeElement(nums, val):
    slow_pointer = 0

    for fast_pointer in range(len(nums)):
        if(nums[fast_pointer] != val):
            nums[slow_pointer] = nums[fast_pointer]
            slow_pointer += 1
    
    print(nums)
    return slow_pointer

print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))