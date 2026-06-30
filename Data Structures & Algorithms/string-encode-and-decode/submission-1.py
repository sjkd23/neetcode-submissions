class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ''
        for x in strs:
            encoded = encoded + str(len(x)) + "#" + x
        return encoded
    def decode(self, s: str) -> List[str]:
        
        decoded = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decoded.append(s[j + 1:j + length + 1])
            i = j + length + 1
        return decoded
            
