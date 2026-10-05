class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window = sum(nums[:k])
        max_sum= window
        for i in range(k,len(nums)):
            window=window-nums[i-k]+nums[i]
            max_sum=max(max_sum,window)
        return max_sum /k