#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result = []
        container = [root]
        while container:
            s = []
            for i in range(len(container)):
                cur = container.pop(0)
                s.append(cur.val)
                if cur.left:container.append(cur.left)
                if cur.right:container.append(cur.right)
            if s:
                result.append(s)
        return result
# @lc code=end

