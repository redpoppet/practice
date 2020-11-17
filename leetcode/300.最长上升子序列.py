#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        dp = [1] * len(nums)
        ans = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
                    ans = max(dp[i],ans)
        return ans 
# @lc code=end

