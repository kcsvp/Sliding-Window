class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res =[0]* len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<t:
                res[stack[-1]] =  i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
        # stack = []
        # sol= []
        # for day in temperatures[::-1]:
        #     span=0
        #     while stack and stack[-1][0]<=day:
        #         span += stack[-1][1]
        #         stack.pop()
        #     if stack :
        #         span += 1
        #     else:
        #         span = 0
        #     sol.append(span)
        #     stack.append((day,span))
        # return sol[::-1]
        # sol = [None]*len(temperatures)
        # stack = []
        # prev_day = None
        # for current_day in range(len(temperatures)):
        #     while len(stack)>0 and (temperatures[stack[-1]]< temperatures[current_day]):
        #         prev_day = stack.pop()
        #         sol[prev_day] = current_day - prev_day
        #     stack.append(current_day)
        # while len(stack)>0:
        #     prev_day = stack.pop()
        #     sol[prev_day] = 0
        # return sol