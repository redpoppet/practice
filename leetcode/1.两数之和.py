#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left in range(len(nums)):
            for right in range(left+1,len(nums)):
                if target == nums[left] + nums[right]:
                    return [left,right]
                else:
                    pass
# @lc code=end

