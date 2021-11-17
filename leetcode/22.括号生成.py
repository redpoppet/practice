#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final_lst = []
        self.back(n,n,"",final_lst)
        return final_lst

    def back(self,left,right,out,lst):
        if left>right or left<0 or right<0:
            return False 
        
        if left==0 and right ==0:
            lst.append(out)
            return True

        self.back(left - 1, right, out + "(", lst);
        self.back(left, right-1, out + ")", lst);   



# @lc code=end

 