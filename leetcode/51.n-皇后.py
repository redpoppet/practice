#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check(queue,row):
            for i in range(row):
                if queue[row]==queue[i] or queue[row] + row == queue[i] + i or queue[row]-row == queue[i]-i:
                    return False
            return True  
    
        def back(queue,row,n):
            if row==n:
                ans = []
                for i in queue:
                    item = '.'*i+'Q'+('.')*(n-1-i)
                    ans.append(item)
                res.append(ans)
            else:
                for i in range(n):
                    queue[row]=i
                    result = check(queue,row)
                    if not result:
                        queue[row]=-1
                        continue
                        
                    else:
                        back(queue,row+1,n)
                        
        res = []
        queue = [-1]*n
        back(queue,0,n)
        return res




# @lc code=end

