#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea_1(self, height: List[int]) -> int:
        max_area = 0 
        for left in range(len(height)):
            for right in range(left+1,len(height)):
                temp_area = min(height[left],height[right])*(right-left)
                max_area = temp_area if temp_area>max_area else max_area
        return max_area 

    def maxArea(self, height: List[int]) -> int:
        max_area = 0 
        left = 0
        right = len(height)-1
        while left < right:
            temp_area = min(height[left],height[right])*(right-left)
            max_area = temp_area if temp_area>max_area else max_area
            if height[left]<height[right]:
                left = left +1
            else:
                right = right -1 
        return max_area 
# @lc code=end

