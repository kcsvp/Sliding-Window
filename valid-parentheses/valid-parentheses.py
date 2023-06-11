class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cursors = {'(':')','{':'}','[':']'}
        for each in s:
            if each in cursors:
                stack.append(each)
                continue
            elif stack == []:
                return False
            elif cursors[stack[-1]] == each:
                    stack.pop()
            else:
                return False

        return stack == []
        