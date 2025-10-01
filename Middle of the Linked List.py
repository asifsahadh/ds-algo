class Solution(object):
    def middleNode(self, head):
        if head is None or head.next is None:
            return head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
