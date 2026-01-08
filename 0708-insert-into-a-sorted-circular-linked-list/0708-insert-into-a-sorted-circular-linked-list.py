"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            new_head = Node(insertVal)
            new_head.next = new_head
            
            return new_head

        curr = head
        while curr.next != head:
            if curr.val <= insertVal <= curr.next.val:
                new_node = Node(insertVal, curr.next)
                
                curr.next = new_node

                return head

            elif curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    new_node = Node(insertVal, curr.next)

                    curr.next = new_node

                    return head

            curr = curr.next

        new_node = Node(insertVal, curr.next)
        curr.next = new_node

        return head