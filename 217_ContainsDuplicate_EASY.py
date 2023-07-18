# solved using HAST SET 

def containsDuplicate(nums):
    hash_set = set()

    for num in nums:
        if(num in hash_set):
            return True
        hash_set.add(num)
        
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))