class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        stack = []
        largest = 0

        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height_index = stack.pop()
                height = heights[height_index]
                
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                
                area = height * width

                largest = max(largest, area)

            stack.append(i)
            
        return largest

