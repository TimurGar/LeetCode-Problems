# Solved with HASH SET (technically not correct as it uses O(n) space)

def singleNumber(nums):
    hash_set = set()

    for num in nums:
        if(num not in hash_set):
                hash_set.add(num)
        else:
             hash_set.discard(num)
        
    return hash_set.pop()

    # correct solution uses XOR

    # Using bitwise XOR (not sure how it works)

    # uniqNum = 0;
    # for idx in nums:
    #     # Concept of XOR...
    #     uniqNum ^= idx;
    #     print("Uniq = " ,uniqNum)
    # return uniqNum;     


# print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
# print(singleNumber([1]))