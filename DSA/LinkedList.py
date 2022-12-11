# PS: You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def disp(l):
    s = ''
    c = l
    while c.next != None:
        s = str(c.val)+s
        c = c.next
    s = str(c.val)+s
    print(s)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        r = l1.val + l2.val
        carry = int(r/10)
        resL = ListNode(r%10,ListNode(0))
        currentL = resL.next
        next1 = l1.next
        next2 = l2.next
        while next1.next!=None and next2.next!=None:
            r = next1.val + next2.val + carry
            carry = int(r/10)
            currentL.value = r%10
            currentL.next = ListNode(0)
            currentL = currentL.next
            next1 = next1.next
            next2 = next2.next
        if next1.next!=None:
            while next1.next!=None:
                r = next1.val + carry
                carry = int(r/10)
                currentL.value = r%10
                currentL.next = ListNode(0)
                currentL = currentL.next
                next1 = next1.next
        if next2.next!=None:
            while next2.next!=None:
                r = next2.val + carry
                carry = int(r/10)
                currentL.value = r%10
                currentL.next = ListNode(0)
                currentL = currentL.next
                next2 = next2.next
        r = next1.val + next2.val + carry
        if r>=10:
            currentL.val = r%10
            currentL.next = ListNode(int(r/10))
        else:
            currentL.val = r
        return resL

l1 = ListNode(val= 2, next= ListNode(val= 4, next= ListNode(val= 7, next= None)))
l2 = ListNode(val= 5, next= ListNode(val= 6, next= ListNode(val= 4, next= None)))

l3 = Solution().addTwoNumbers(l1,l2)

disp(l1)
disp(l2)
disp(l3)