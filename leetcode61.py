# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 节点为空或仅有一个节点
        if not head or not head.next or k == 0:
            return head

        # 设置一个虚拟头节点
        node = ListNode(-float('inf'))
        node.next = head
        head = node

        p = ListNode()  # 标记新前端末尾的节点
        q = ListNode()  # 标记新链表末尾的节点
        start = ListNode()  # 标记新后端起始的节点

        start = head.next
        q = start
        p = start
        count = k
        # 寻找k间隔
        while count:
            if not p.next:
                count = k % (k-count+1)
                p = start
            else:
                p = p.next
                count -= 1

        if p == q:
            return head.next

        # 将指针移到后k位
        while p.next:
            p = p.next
            q = q.next

        # 重新连接链表
        head.next = q.next
        p.next = start
        q.next = None
        return head.next
