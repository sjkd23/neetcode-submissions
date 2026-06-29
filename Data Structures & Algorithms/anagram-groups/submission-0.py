class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}

        for x in strs:
            sorted_x = "".join(sorted(x))
            if sorted_x not in strs_dict:
                strs_dict[sorted_x] = [x]
            else: 
                strs_dict[sorted_x].append(x)
        return list(strs_dict.values())