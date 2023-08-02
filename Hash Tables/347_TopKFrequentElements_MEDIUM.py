# Solved with HASH MAP

# mine worked but it was slow
# O(n) solution
def topKFrequent(nums, k):
    count = {}
    # creating a subarray to store all the items of the same frequency
    freq = [[] for i in range(len(nums) + 1)]
    res = []

    # easy way of counting freq of each number
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    
    # .items() gives the key : value pairs
    for num, count in count.items():
        freq[count].append(num)

    # starting from the back of freq arr, to get the items with highest items
    for i in range(len(freq)-1, 0, -1):
        # iterating through every item in each freq (in case there are a few)
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))

