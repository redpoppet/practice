#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result  = []
        if root is not None:
            
            print(root.left)
            print(root.right)
            if root.left is not None:
                result.extend(self.inorderTraversal(root.left))
            result.append(root.val)
            if root.right is not None:
                result.extend(self.inorderTraversal(root.right))
            
        return result 

# @lc code=end

