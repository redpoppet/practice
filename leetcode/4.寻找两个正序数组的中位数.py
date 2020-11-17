#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # return nums1[0]
        new_list,n = self.merge_(nums1,nums2)
        # n = len(new_list)
        if n%2==0:
            print(n)
            print(new_list)
            return (new_list[n//2] + new_list[n//2-1])/2
        else:
            return new_list[n//2]

    def merge_(self,nums1,nums2):

        nums1.extend(nums2)
        nums1.sort()
        return nums1,len(nums1)

# @lc code=end

