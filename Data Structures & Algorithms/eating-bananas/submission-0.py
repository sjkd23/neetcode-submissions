class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        

        left = 1
        right = max(piles)

        lowest = max(piles)

        while left <= right:
            total_hours = 0
            mid = (right + left) // 2

            for pile in piles:
                total_hours += math.ceil(pile / mid)
            
            if total_hours > h:
                left = mid + 1
            else:
                lowest = mid
                right = mid - 1
        return lowest

