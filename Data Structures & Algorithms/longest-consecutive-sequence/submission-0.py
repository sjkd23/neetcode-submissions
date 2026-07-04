class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) < 1:
            return 0
        nums_set = set(nums)
        highest = 0
        for num in nums_set:
            counter = 1
            if num - 1 not in nums_set:
                while num + 1 in nums_set:
                        counter += 1
                        num += 1
            if highest < counter:
                highest = counter
        return highest



                
