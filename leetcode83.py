# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        node = ListNode()
        node.val = -float('inf')
        node.next = head
        head = node

        p = ListNode()
        tag = ListNode()

        tag = head
        p = tag.next

        while p:
            if p.val == tag.val:
                p = p.next
            else:
                tag.next = p
                tag = p
                p = p.next
        if tag.next != p:
            tag.next = p
        return head.next
