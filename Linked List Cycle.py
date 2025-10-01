class Solution(object):
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        seen = set()
        while head: # we use head, which is the node reference, becuase memory address won't repeat. so if it points back to the same address, this means there is a loop.
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
