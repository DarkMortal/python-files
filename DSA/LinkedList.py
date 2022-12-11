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
        while next1.next!=None or next2.next!=None:
            r = next1.val + next2.val + carry
            carry = int(r/10)
            currentL.val = r%10
            currentL.next = ListNode(0)
            currentL = currentL.next
            next1 = (ListNode(0) if next1.next == None else next1.next)
            next2 = (ListNode(0) if next2.next == None else next2.next)
            
        r = next1.val + next2.val + carry
        if r>=10:
            currentL.val = r%10
            currentL.next = ListNode(int(r/10))
        else:
            currentL.val = r
        return resL

l1 = ListNode(val= 2, next= ListNode(val= 4, next= ListNode(val= 7)))
l2 = ListNode(val= 5, next= ListNode(val= 6, next= ListNode(val= 4)))
l3 = ListNode(val= 2, next= ListNode(val= 4, next= ListNode(val= 7, next= ListNode(5))))
l4 = ListNode(val= 5, next= ListNode(val= 6, next= ListNode(val= 4, next= ListNode(4, next= ListNode(3)))))

disp(l1)
disp(l2)
print()

disp(l3)
disp(l4)
print()

l2 = Solution().addTwoNumbers(l1,l2)
l4 = Solution().addTwoNumbers(l4,l3)

disp(l2)
disp(l4)

print()
l4 = Solution().addTwoNumbers(l4,l2)
disp(l4)

'''Output
742
465

5742
34465

1207
40207

41414
'''