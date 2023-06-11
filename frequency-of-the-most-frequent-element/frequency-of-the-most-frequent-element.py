class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l,sum,sol = 0,0,0
        nums.sort()
        for r,n in enumerate(nums):
            sum += n
            if (r-l+1)*n - sum > k:
                sum -= nums[l]
                l += 1
            else:
                sol = max(r-l+1,sol)
        return sol
                

            
