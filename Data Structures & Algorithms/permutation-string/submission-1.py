from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        l = 0
        r = len(s1)

        counts = Counter(s1)

        window = dict()

        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1

        while r <= len(s2):
            if counts == window:
                return True
            if r == len(s2):
                return False
            else:
                window[s2[l]] = window.get(s2[l], 0) - 1
                if window[s2[l]] == 0:
                    window.pop(s2[l])
                l += 1

                window[s2[r]] = window.get(s2[r], 0) + 1
                r += 1
        return False
