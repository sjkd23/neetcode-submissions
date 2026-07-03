class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0

        longest = 0
        check = {}
        max_fre = 0
        while r < len(s):
            check[s[r]] = check.get(s[r], 0) + 1
            if check[s[r]] > max_fre:
                max_fre = check[s[r]]
            length = r - l + 1
            if length - max_fre > k:
                
                check[s[l]] -= 1
                l += 1
            else:
                if longest < length:
                    longest = length
            r += 1
        return longest
