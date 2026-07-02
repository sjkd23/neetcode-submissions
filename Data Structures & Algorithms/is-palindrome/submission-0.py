
class Solution:
    def isPalindrome(self, s: str) -> bool:

        pointer_s = 0
        pointer_e = len(s) - 1

        while pointer_s <= pointer_e:
            while pointer_s <= pointer_e and s[pointer_s].isalnum() is False:
                pointer_s += 1
            while pointer_s <= pointer_e and s[pointer_e].isalnum() is False:
                pointer_e -= 1
            if pointer_s > pointer_e:
                return True
            if s[pointer_s].lower() != s[pointer_e].lower():
                return False
            pointer_s += 1
            pointer_e -= 1
        return True

        
