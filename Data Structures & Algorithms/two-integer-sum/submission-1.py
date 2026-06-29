class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        new_dict = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in new_dict:
                return [new_dict[complement], index]
            new_dict[value] = index