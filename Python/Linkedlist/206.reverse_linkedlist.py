# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head):
        curr,prev=head,None

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        return prev


head = ListNode(1)
head.next = ListNode(7)
head.next.next = ListNode(3)
head.next.next.next = ListNode(6)

s1=Solution()
res=s1.reverseList(head)

current = res
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
