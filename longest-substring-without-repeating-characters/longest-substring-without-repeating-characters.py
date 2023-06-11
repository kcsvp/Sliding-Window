class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        vdict ,l,longest= dict(),0,0
        for i in range(len(s)):
            while s[i] in vdict:
                vdict.pop(s[l])
                l += 1
            vdict[s[i]] = 1
            longest = max(longest,len(vdict))
        return longest
            
        # temp = s[0]
        # longest = 1
        # for i in range(1,len(s)):
        #     if s[i] not in temp:
        #         temp += s[i]
        #         longest = max(len(temp),longest)
        #     else:
        #         while s[i] in temp:
        #             temp = temp[1:]
        #         temp += s[i]
        # return longest
