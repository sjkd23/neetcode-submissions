class Solution:
    def trap(self, height: List[int]) -> int:

        s = 0
        e = len(height) - 1

        left_max = height[s]
        right_max = height[e]
        water = 0
        while s < e:
            if left_max < right_max:
                s += 1
                if height[s] > left_max:
                    left_max = height[s]
                else:
                    water += left_max - height[s]

            else:
                e -= 1
                if height[e] > right_max:
                    right_max = height[e]
                else:
                    water += right_max - height[e]

        return water
