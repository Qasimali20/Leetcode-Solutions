class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def removeElements(self, head, val):
        dummy=ListNode(0)
        dummy.next=head
        curr, prev = head,dummy

        while curr:
            if curr.val == val:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return dummy.next
    
head=ListNode(1)
head.next=ListNode(9)
head.next.next=ListNode(6)
head.next.next.next=ListNode(5)
head.next.next.next.next=ListNode(2)

s=Solution()

new_head = s.removeElements(head, 6)

current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")