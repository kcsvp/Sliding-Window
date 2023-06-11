class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [int(tokens[0])]
        if len(tokens)>2:
            for i in tokens[1:]:
                if i[-1].isnumeric():
                    stack.append(int(i))
                else:
                    var2 = stack.pop()
                    var1 = stack.pop()
                    if i == '-':
                        stack.append(var1-var2)
                    elif i == '+':
                        stack.append(var1 + var2)
                    elif i == '*':
                        stack.append(var1 * var2)
                    elif i == '/':
                        stack.append(int(var1/var2))
        return stack[0]