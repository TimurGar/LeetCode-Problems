# Solved with HASH SET
# Beats 99.69%

# Notes
# go through each char in jewels and add the to hash set
# go through each stone and compare if it's in set and if so add count

def numJewelsInStones(jewels, stones):
    types = set(jewels)
    count = 0

    for stone in stones:
        if stone in types:
            count += 1
    
    return count


print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "Z"))

