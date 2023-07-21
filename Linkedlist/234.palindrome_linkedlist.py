class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def isPalindrome(self, head):
        fast=head
        slow=head
        prev=None

        while fast and fast.next:
          fast=fast.next.next
          slow=slow.next

        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp

        left,right=head, prev
        
        while right:

            if left.val != right.val:
                return False

            left=left.next
            right=right.next
        return True 
    
# Create a sample palindrome linked list: 1 -> 2 -> 3 -> 2 -> 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

s1=Solution()
is_palindrome=s1.isPalindrome(head)
print(is_palindrome)  # Output: True
