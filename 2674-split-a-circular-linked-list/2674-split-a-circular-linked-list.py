
class ListNode(object):
    def __init__(self, value = 0, next = None):
        pass


class Solution(object):
    def splitCircularLinkedList(self, list):
        head1 = list
        slow, fast = head1, head1.next
        while head1 != fast.next:
            slow = slow.next
            fast = fast.next.next if head1!=fast.next.next else fast.next
        head2 = slow.next
        slow.next = head1
        fast.next = head2

        return [head1, head2]

