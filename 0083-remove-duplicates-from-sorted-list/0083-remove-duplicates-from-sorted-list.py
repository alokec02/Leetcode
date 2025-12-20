# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head
        prev_node = dummy
        curr_node = head

        while curr_node:
            if curr_node.val in seen:
                prev_node.next = curr_node.next
            else:
                seen.add(curr_node.val)
                prev_node = curr_node
            curr_node = curr_node.next
        return dummy.next
