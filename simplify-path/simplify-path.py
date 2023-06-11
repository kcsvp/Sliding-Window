class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for each in path.split('/'):
            if each == '..':
                if stack:
                    stack.pop()
            elif each and each and each != '.' and each != '/':
                stack.append(each)
        
        return '/' + '/'.join(stack)