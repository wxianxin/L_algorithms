# Author: Steven Wang    Date: 20170408
# 2 add_two_numbers

# What is learned: Try not t create Node before you have its value, in this way you need less lines.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)

l1.next = l2
l2.next = l3

l2 = ListNode(4)
l3 = ListNode(5)
l4 = ListNode(6)

l2.next = l3
l3.next = l4

###########################
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    _ = ListNode(0)
    r = _
    carry = 0
  

    while l1 != None or l2 != None:

        if l1 == None:
            l1 = ListNode(0)
        if l2 == None:
            l2 = ListNode(0)

        if l1.val + l2.val + carry >= 10:
            _.val = l1.val + l2.val + carry - 10
            carry = 1
        else:
            _.val = l1.val + l2.val + carry
            carry = 0

        l1 = l1.next
        l2 = l2.next

        second_last = _
        new = ListNode(0)
        _.next = new
        _ = new

    if carry == 1:
        _.val = 1
    else:
        second_last.next = None

    return r

addTwoNumbers(l1, l2)








    