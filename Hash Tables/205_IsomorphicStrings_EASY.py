# Solved with HASH MAP

# Notes
# char : char, e : a
# s -> t
# check if the char exists in HM, if not add and move on
# if yes, compare with the t val, if similar continue, if not -> false

def isIsomorphic(s, t):
    map = {}

    if len(s) != len(t):
        return False

    for ind, char in enumerate(s):

        if char in map:
            # checking if the mapped val is the same as t val
            if map[char] != t[ind]:
                return False
        else:
            # making sure no two characters map to the same character
            if t[ind] in map.values():
                return False
            else:
                # e : a
                map[char] = t[ind]
            
    return True

print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("badc", "baba")) # exp false