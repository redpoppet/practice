#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class Solution:
#     def nextLargerNodes(self, head: ListNode) -> List[int]:
#         result = list()
#         while head:
#             val = head.val
#             item = 0
#             point = head
#             while point.next:
#                 if point.next.val>val:
#                     item = point.next.val 
#                     break;   
                
#                 point = point.next


#             result.append(item)

#             head = head.next     
#         return result
        

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:        
        nums = []
        node = head
        while node != None :
            nums.append(node.val)
            node = node.next

        stack = []
        stack_loc = []
        res = [0] * len(nums)

        for i in range(len(nums)):
            print(nums[i])
            while stack and stack[-1] < nums[i]:
                print(nums[i],stack[-1])
                res[stack_loc[-1]] = nums[i]
                stack.pop()
                stack_loc.pop()

            stack.append(nums[i])
            stack_loc.append(i)

        return res  


            
# @lc code=end

