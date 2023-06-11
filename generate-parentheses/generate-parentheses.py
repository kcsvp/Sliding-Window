class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        stack = []
        def dfs(stack,open_c,close_c):
            # print('inside',stack,open_c,close_c)
            if close_c == n:
                # print('end ',stack)
                sol.append("".join(stack))
                return
            if open_c < n:
                stack.append('(')
                dfs(stack,open_c + 1,close_c)
                stack.pop()

            if open_c > close_c:
                stack.append(')')
                dfs(stack,open_c,close_c + 1)
                stack.pop()

            

        dfs(stack,0,0)
        return sol

        

