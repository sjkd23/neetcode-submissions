class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []

        for position, speed in cars:
            turns = (target - position) / speed

            if not stack or turns > stack[-1]:
                stack.append(turns)

        return len(stack)

