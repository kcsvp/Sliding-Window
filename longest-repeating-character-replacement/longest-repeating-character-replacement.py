class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sol = 0
        l,maxf,cdict = 0,0,dict()
        for r,c in enumerate(s):
            cdict[c] = cdict.get(c,0) + 1
            maxf = max(maxf,cdict[c])
            if (r-l+1) - maxf > k:
                cdict[s[l]] -= 1
                l += 1
            sol = max(sol,r-l+1)
        return sol

