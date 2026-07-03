class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        longest = 0
        check = set()
        while r < len(s):
            while s[r] in check:
                check.remove(s[l])
                l += 1
            
            check.add(s[r])
            if longest < r - l + 1:
                longest = r - l + 1
            
            r += 1
        return longest
