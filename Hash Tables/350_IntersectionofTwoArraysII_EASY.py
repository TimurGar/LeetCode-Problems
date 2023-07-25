# Solved with HASH MAP

# num : count
# nums1 - longest
def intersect(nums1, nums2):
    map = {}
    res = []
    
    if(len(nums1) < len(nums2)):
        nums1, nums2 = nums2, nums1

    for i in range(len(nums1)):
        if nums1[i] in map:
            map[nums1[i]] += 1
        else:
            map[nums1[i]] = 1
    
    for i in range(len(nums2)):
        if nums2[i] in map and map[nums2[i]] != 0:
            res.append(nums2[i])
            map[nums2[i]] -= 1

    return res

print(intersect([1,2,2,1], [2,2]))
print(intersect([4,9,5], [9,4,9,8,4]))
print(intersect([1,2], [1,1]))