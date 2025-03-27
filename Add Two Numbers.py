# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
      
def addTwoNumbers(l1, l2):

    lst1 = []
    temp1 = l1
    while temp1.next is not None:
        lst1.append(temp1.val)
        temp1 = temp1.next
    lst1.append(temp1.val)

    lst2 = []
    temp2 = l2
    while temp2.next is not None:
        lst2.append(temp2.val)
        temp2 = temp2.next
    lst2.append(temp2.val)

    s1 = ''
    lst1_ = [str(ele) for ele in lst1]
    for i in range(len(lst1_)):
        s1 += lst1_.pop(-1)

    s2 = ''
    lst2_ = [str(ele) for ele in lst2]
    for i in range(len(lst2_)):
        s2 += lst2_.pop(-1)

    resp = int(s1) + int(s2)
    resp_ = str(resp)

    resp__ = [int(ele) for ele in resp_][::-1]

    head = ListNode(resp__[0])
    temp = head
    for i in range(1, len(resp__)):
        temp.next = ListNode(resp__[i])
        temp = temp.next
    
    return head
