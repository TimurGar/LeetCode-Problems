# Solved with HASH MAP
# Cool Easy Iteration in Hash
# copied for online, my didn't work :(

def containsNearbyDuplicate(nums, k):
    map = {}

    # Traverse for all elements of the given array in a for loop...
    for i in range(len(nums)):

        # If duplicate element is present at distance less than equal to k, return true...
        if nums[i] in map and abs(i - map[nums[i]]) <= k:
            return True
        
        # add num and it's index to hash map
        map[nums[i]] = i

    return False


print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))