class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_right_to_left = sorted(zip(position, speed), reverse=True)
        stack = []

        for i in range(len(position)):
            time_to_reach = (target - cars_right_to_left[i][0]) / cars_right_to_left[i][1]
            if stack and stack[-1] < time_to_reach:
                stack.append(time_to_reach)
            if not stack:
                stack.append(time_to_reach)
        
        return len(stack)
