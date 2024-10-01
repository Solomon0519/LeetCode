# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return

        t = head
        s = head
        n = head
        c = s.next

        while c:
            s = c
            c = c.next
            s.next = n
            n = s

        t.next = None
        return s


# More efficient solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = head

        while current_node:

            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        return previous_node
