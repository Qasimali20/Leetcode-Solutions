class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None

        #dummy = ListNode(0,head)
        slow = head
        fast = head.next.next

        # Move the fast pointer two steps at a time and the slow pointer one step at a time
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Update the slow.next pointer before deleting the middle node
        slow.next = slow.next.next

        return head
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
#head.next.next.next.next = ListNode(5)
#head.next.next.next.next.next = ListNode(6)
#head.next.next.next.next.next.next = ListNode(7)

# Create an object of the Solution class
solution = Solution()

# Call the deleteMiddle method on the solution object
new_head = solution.deleteMiddle(head)

# Output the modified linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
