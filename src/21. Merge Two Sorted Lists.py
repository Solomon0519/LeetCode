# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None

        if not list1:
            return list2
        if not list2:
            return list1

        list1_pointer = list1
        list2_pointer = list2

        if list1_pointer.val >= list2_pointer.val:
            head = list2_pointer
            list2_pointer = list2_pointer.next
        else:
            head = list1_pointer
            list1_pointer = list1_pointer.next

        current_node = head

        while list1_pointer or list2_pointer:

            if (not list1_pointer):
                current_node.next = list2_pointer
                break
            if (not list2_pointer):
                current_node.next = list1_pointer
                break

            if (list1_pointer.val >= list2_pointer.val):
                current_node.next = list2_pointer
                list2_pointer = list2_pointer.next
                current_node = current_node.next
            else:
                current_node.next = list1_pointer
                list1_pointer = list1_pointer.next
                current_node = current_node.next

        return head