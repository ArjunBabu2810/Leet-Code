# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        head = ListNode()
        cur=head
        while l1 or l2 or c:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
            c=0
            if s > 9:
                c = 1
                s-=10
            cur.next = ListNode(s)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next