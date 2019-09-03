"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pHead = ListNode(None)
        pHead.next = head

        cur = pHead
        count = 1
        while count <= n:
            cur = cur.next
            count += 1

        cur_ = pHead
        while cur.next is not None:
            cur = cur.next
            cur_ = cur_.next
        cur_.next = cur_.next.next
        return pHead.next

