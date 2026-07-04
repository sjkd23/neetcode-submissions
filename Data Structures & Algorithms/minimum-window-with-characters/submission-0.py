from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        check = Counter(t)
        window = {}

        l = 0

        need = len(check)
        have = 0

        lowest = float("inf")
        shortest = ""

        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in check and window[char] == check[char]:
                have += 1

            while have == need:
                if lowest > r - l + 1:
                    lowest = r - l + 1
                    shortest = s[l:r + 1]

                left_char = s[l]

                if left_char in check and window[left_char] == check[left_char]:
                    have -= 1

                window[left_char] -= 1
                if window[left_char] < 1:
                    window.pop(left_char)
                l += 1

        return shortest
