# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=head
        j=head
        for k in range(n):
            j=j.next
        if j==None:
            return head.next
        while j.next!=None:
            i=i.next
            j=j.next
        i.next=i.next.next
        return head
        