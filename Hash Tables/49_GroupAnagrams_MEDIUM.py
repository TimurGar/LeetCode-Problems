# Solved with HASH MAP with a DESIGNED KEY
# beats 94.7%

# sort each string in the arr
# populate the hashmap 
# sorted_str : group 

def groupAnagrams(strs):

    if len(strs) > 1:
        map = {}
        sorted_str = ""
        # eat
        for i in range(len(strs)):
            # Creating a key (by sorting a string)
            sorted_str = "".join(sorted(strs[i]))
            # aet
            if sorted_str in map:
                map[sorted_str].append(strs[i])
            else:
                map[sorted_str] = [strs[i]]

        return map.values()
    else:
        return [strs]


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))


    