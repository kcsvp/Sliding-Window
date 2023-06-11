class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for each in asteroids:
            if each > 0:
                stack.append(each)
            else:
                while stack and stack[-1]>0 and stack[-1] < abs(each):
                    stack.pop()
                if stack and stack[-1]>0 and  stack[-1] == abs(each):
                    stack.pop()
                elif not stack or stack and stack[-1]<0:
                    stack.append(each)
        return stack
        # while len(asteroids)>1:
        #     as2 = asteroids.pop()
        #     as1 = asteroids.pop()
        #     if as1>0 and as2<0:
        #         if abs(as1) > abs(as2):
        #             asteroids.append(as1)
        #         elif abs(as1) < abs(as2):
        #             asteroids.append(as2)
        #         else:
        #             continue
        #     else:
        #         asteroids.append(as1)
        #         temp = [as2] + temp
            
        # return asteroids + temp
