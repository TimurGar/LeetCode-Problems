# Solved with FAST & SLOW POINTERS Approach
 
# Notes slow and fast pointer technique

def removeDuplicates(nums):
    slow_ind = 0
    k = 1
    
    for i in range(len(nums)):

        if(nums[i] > nums[slow_ind]):
            nums[slow_ind+1] = nums[i]
            slow_ind += 1
            k += 1

    print(nums)
    return k


print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

