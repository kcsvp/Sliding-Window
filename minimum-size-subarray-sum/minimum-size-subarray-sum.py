class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sol,sum1,l=math.inf,0,0
        for r in range(len(nums)):
            sum1 += nums[r]
            while l<=r and sum1 >= target:
                sol = min(r-l+1,sol)
                sum1 -= nums[l]
                l+=1
        if sol == math.inf:
            return 0
        return sol