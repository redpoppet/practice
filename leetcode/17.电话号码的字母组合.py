#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:return []
        map = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        # result = list().extend(map[digits[0]])
        result = ['']
        
        for ch in digits:
            result_temp = [ x+y for x in result for y in map[ch]]
            result = result_temp
        return result


# @lc code=end

