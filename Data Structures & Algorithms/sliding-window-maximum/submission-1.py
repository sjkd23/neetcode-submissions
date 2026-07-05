from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()
        
        highest = []

        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        highest.append(nums[q[0]])

        l = 1 
        r = k

        while r < len(nums):
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
            if q and q[0] < l:
                q.popleft()
            q.append(r)
            highest.append(nums[q[0]])
            r += 1
            l += 1
        return highest
            