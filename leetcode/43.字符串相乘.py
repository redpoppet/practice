#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        s = 0 
        for i in  range(len(num1)):
            for j in range(len(num2)):
                item_1 = int(num1[i])*pow(10,len(num1)-1-i)
                item_2 = int(num2[j])*pow(10,len(num2)-1-j)
                mul = item_1 * item_2
                # print(mul)
                s = s + mul
        return str(s) 

# @lc code=end

