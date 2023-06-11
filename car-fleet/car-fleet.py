class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = [ (position[i],speed[i]) for i in range(len(position))]
        data = sorted(data,reverse = True)
        distance = target - data[0][0]
        total_time = distance/data[0][1]
        stack = [total_time]
        i = 1
        while i < len(position):
            distance = target - data[i][0]
            total_time = distance/data[i][1]
            if stack[-1] < total_time:
                stack.append(total_time)
            i += 1
        return len(stack)