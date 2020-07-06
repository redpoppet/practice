#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# 遍历字符串中的每个字符
#判断当前字符为首的所有子串是否有重复字符，如果无，则将当前子串的长度赋值给max
#否则，跳过

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        for left in range(len(s)):
            for right in range(left,len(s)+1):
                if self.hasSameCharacter(s[left:right]):
                    break
                else:
                    len_temp = len(s[left:right])
                    if len_temp > max:
                        max = len_temp 
                
        return max 
    
    def hasSameCharacter(self,s:str) -> bool:
        return len(s)!=len(set(s))


# if __name__ == "__main__":
#     a = Solution()
#     print(a.lengthOfLongestSubstring("au"))

# @lc code=end

