class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            pointer_s = i + 1
            pointer_e = len(nums) - 1
            while pointer_s < pointer_e:
                num_sum = nums[pointer_s] + nums[pointer_e] + nums[i]
                if num_sum == 0:
                    triplet = [nums[pointer_s], nums[pointer_e], nums[i]]
                    triplets.append(triplet)
                    pointer_s += 1
                    while nums[pointer_s] == nums[pointer_s - 1] and pointer_s < pointer_e:
                        pointer_s += 1
                    pointer_e -= 1
                    while nums[pointer_e] == nums[pointer_e + 1] and pointer_s < pointer_e:
                        pointer_e -= 1
                elif num_sum < 0:
                    pointer_s += 1
                elif num_sum > 0:
                    pointer_e -= 1
        return triplets
