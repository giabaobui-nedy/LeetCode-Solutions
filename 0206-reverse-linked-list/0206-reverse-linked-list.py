# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        pt = head
        while pt:
            stack.append(pt.val)
            pt = pt.next
        pt = head
        while stack:
            pt.val = stack.pop()
            pt = pt.next
        return head
