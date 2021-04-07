# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 只有一个节点，直接返回
        if head.next is None:
            return head
        # 添加一个虚拟头结点
        node = ListNode()
        node.val = -float('inf')
        node.next = head
        head = node

        p = ListNode()
        q = ListNode()
        tag = ListNode()

        q = head
        tag = q.next
        p = tag.next
        while p:
            if p.val == tag.val:
                p = p.next
            else:
                if tag.next == p:
                    q = tag
                    tag = p
                    p = p.next
                else:
                    q.next = p
                    tag = p
                    p = p.next
        if tag.next != p:
            q.next = p
        return head.next

