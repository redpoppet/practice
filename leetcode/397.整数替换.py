#
# @lc app=leetcode.cn id=397 lang=python3
#
# [397] 整数替换
#

# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0 
        while n>1:
            print(n)
            if n==3:
                n-=1
            elif n%4==1:
                n = n-1
            elif n%4==3:
                n = n+1
            else:
                n = n//2
            count = count+1
        return count
            


# @lc code=end

