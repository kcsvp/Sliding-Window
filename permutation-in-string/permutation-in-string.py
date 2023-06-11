class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1,c1= len(s1),Counter(s1)
        c2 = Counter(s2[:l1])
        if c1 == c2:
            return True
        for i in range(l1,len(s2)):
            if c2[s2[i-l1]] == 1:
                c2.pop(s2[i-l1])
            else:
                c2[s2[i-l1]] -= 1
            c2[s2[i]] = c2.get(s2[i],0) + 1
            if c2 == c1:
                return True
        return False