#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        lst = list()
        while head:
            lst.append(head.val)
            head= head.next
        lst.pop(-n)
        if len(lst)==0: return []
        head = ListNode()
        first = head
        while lst:
            first.val = lst.pop(0)
            if lst:
                first.next = ListNode() 
                first = first.next
        return head 

# @lc code=end

