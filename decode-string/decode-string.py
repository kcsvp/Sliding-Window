class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == ']':
                char = ''
                num = ''
                while stack[-1]!='[':
                    char = stack.pop() + char
                stack.pop()
                while stack != [] and stack[-1] in '0123456789':
                    num += stack.pop()
                num = int(num[::-1])
                for _ in range(num):
                    stack.append(char)
            else:
                stack.append(s[i])
            i += 1
        return ''.join(stack)
