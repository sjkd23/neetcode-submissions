class Solution:
    def maxArea(self, heights: List[int]) -> int:

        s = 0
        e = len(heights) - 1

        container = 0

        while s < e:
            current = (e - s) * min(heights[e], heights[s])

            if heights[s] < heights[e]:
                s += 1

            else:
                e -= 1

            container = max(container, current)

        return container
