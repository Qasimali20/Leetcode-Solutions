# Definition for singly-linked list.
class ListNode:
      def __init__(self, val=0, next=None):
          self.val = val
          self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0,head)
        left=dummy
        right=head

        while n>0 and right:
            right=right.next
            n-=1

        while right:
            right=right.next
            left=left.next
        
        left.next=left.next.next

        return dummy.next
    
# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2

# Create an object of the Solution class
s1 = Solution()

# Call the removeNthFromEnd method
new_head = s1.removeNthFromEnd(head, n)

# Output: 1 -> 2 -> 3 -> 5
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
