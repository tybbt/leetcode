# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 空链表, 接下来链表中至少有一个元素
        if head.next == None:
            return head
        #无需翻转元素
        if left == right:
            return head
        distance = right - left
        memoryStack = []    # 存放需要翻转的数据
        start = ListNode()  # 标记左端点翻转数据起始位置
        p = ListNode()      # 用于搜寻的节点
        p = head
        # 先找到左端点
        left -= 1
        right -= 1
        while left:
            if p is not None:
                p = p.next
                left -= 1
            else:
                # 链表长度小于left
                return None
        # 标记翻转起始点
        start = p
        # 找到右端点
        while distance:
            if p is not None:
                memoryStack.append(p.val)
                p = p.next
                distance -= 1
            else:
                # 链表长度小于right-1
                return None
        if p is not None:
            memoryStack.append(p.val)
        else:
            # 链表长度小于right
            return None
        # 出栈从start翻转列表元素
        while start != p:
            start.val = memoryStack.pop()
            start = start.next
        start.val = memoryStack.pop()
        return head

    def reverseByLink(self, head: ListNode, left: int, right: int) -> ListNode:
        # 空链表, 接下来链表中至少有一个元素
        if head.next == None:
            return head
        #无需翻转元素
        if left == right:
            return head
        distance = right - left
        node = ListNode()
        node.next = head
        head = node
        start = ListNode()
        subhead = ListNode()
        p = ListNode()
        p = head
        while left-1:
            if p is not None:
                p = p.next
                left -= 1
            else:
                return None
        start = p
        p = p.next
        subhead = p
        while distance:
            if p.next is not None:
                start.next = p.next
                p.next = p.next.next
                start.next.next = subhead
                subhead = start.next
                distance -= 1
            else:
                return None
        return head.next


head = ListNode(1, None)
p = ListNode()
p = head
for i in range(2, 6):
    node = ListNode(i, None)
    p.next = node
    p = p.next
p = head
while p is not None:
    print(p.val, end='')
    p = p.next
sv = Solution()
newhead = sv.reverseByLink(head, 2, 4)
p = newhead
while p is not None:
    print(p.val, end='')
    p = p.next
