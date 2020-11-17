#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和

import tracemalloc



# ... run your application ...


# @lc code=start
class Solution:
    def threeSumClosest(self, nums, target) -> int:

        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for index in range(len(nums)):
            left  = index + 1
            right = len(nums) -1
            while left<right:
                cuur_sum = nums[index]+nums[left] + nums[right]
                if abs(cuur_sum-target) < abs(result-target):
                    result = cuur_sum
                if cuur_sum - target < 0:
                    left = left + 1
                elif cuur_sum - target>0 :
                    right = right - 1
                else:
                    return target                
        return result 



# @lc code=end



if __name__ == "__main__":
    tracemalloc.start()
    s = Solution()
    result = s.threeSumClosest([1,2,3],0)
    print(result)
    print("[ Top 10 ]")

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    for stat in top_stats[:10]:
        print(stat)
 
