
# Notes
# if not 0, switch with slow pointer, move the pointer

def moveZeroes(nums):
    
    slow_ind = 0
    for i in range(len(nums)):
  
        if(nums[i] != 0):
            # swapping values without the creation of temp variable 
            # (slower than the conventional way)
            nums[i], nums[slow_ind] = nums[slow_ind], nums[i]
            slow_ind += 1

    return nums

print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0]))
