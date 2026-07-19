class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        left = 0
        right = len(nums1)
        total_left = (len(nums1) + len(nums2) + 1) // 2

        while left <= right:

            cut1 = (left + right) // 2
            cut2 = total_left - cut1

            left1_max = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            right1_min = float("inf") if cut1 == len(nums1) else nums1[cut1]

            left2_max = float("-inf") if cut2 == 0 else nums2[cut2 - 1]
            right2_min = float("inf") if cut2 == len(nums2) else nums2[cut2]

            if left1_max <= right2_min and left2_max <= right1_min:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (min(right1_min, right2_min) + max(left1_max, left2_max)) / 2 
                else:
                    return max(left1_max, left2_max)
            elif left1_max > right2_min:
                right = cut1 - 1
            else:
                left = cut1 + 1
