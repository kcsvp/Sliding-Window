class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack1 = []
        stack2 = []
        for i,c in enumerate(s):
            if stack1 and stack1[-1] == c:
                stack2[-1]+=1
            else:
                stack1.append(c)
                stack2.append(1)
            while stack1 and stack2[-1]>=k:
                stack1.pop()
                stack2.pop()
        
        return ''.join([c*n for c,n in zip(stack1,stack2)])
            

                
                

