# Solved with SLIDING WINDOW and HASH SET
# could have solved it, after I got the idea of who to do a sliding window

def lengthOfLongestSubstring(s):
    substring = set()
    longest = 0
    left = 0

    for right in range(len(s)):
        while s[right] in substring:
            substring.remove(s[left])
            left += 1

        substring.add(s[right])
        longest = max(longest, right - left + 1)
    
    return longest
        

print(lengthOfLongestSubstring("abcabcbb")) 
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("aab")) 
print(lengthOfLongestSubstring("dvdf"))            