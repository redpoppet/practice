#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        result = list()
        for a in range(len(nums)-2):
            if nums[a]>0:break
            if a > 0 and nums[a] == nums[a - 1]: continue
            b,c = a+1,len(nums)-1
            while b<c:
                s = nums[a] + nums[b] +nums[c]
                # print(a,b)
                if s<0:
                    b=b+1
                    while b<c and nums[b]==nums[b-1]: b=b+1
                elif s>0:
                    c=c-1
                    while b<c and nums[c]==nums[c+1]: c=c-1
                else:
                    result.append([nums[a],nums[b],nums[c]])  
                    b=b+1
                    c=c-1
                    while b<c and nums[b]==nums[b-1]:b = b+1
                    while b<c and nums[c]==nums[c+1]:c=c-1

                
        
        return result



# @lc code=end

