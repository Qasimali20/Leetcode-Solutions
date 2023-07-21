class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def middleNode(self, head):
        
        slow, fast=head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
#head.next.next.next.next.next = ListNode(6)

solution = Solution()

# Call the middleNode method on the solution object
middle_node = solution.middleNode(head)

# Output the middle node and the subsequent nodes
current = middle_node
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")