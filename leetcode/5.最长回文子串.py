#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        str_huiwen = ""
        for left in range(len(s)):
            for right in range(len(s)+1,left,-1):
                if self.isHuiWen(s[left:right]):
                    break
            if len(s[left:right])>max_len:
                max_len = len(s[left:right])
                str_huiwen = s[left:right]
                    
                    
        return str_huiwen

    def isHuiWen(self,s:str) -> str:
        return s==s[::-1]

                    
                
                    
                

# @lc code=end

