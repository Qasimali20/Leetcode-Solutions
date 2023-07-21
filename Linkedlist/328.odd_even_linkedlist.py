class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head:
            return head

        odd = head
        even = head.next

        # Maintain the even head
        evenHead = even

        while even and even.next:
            # Change pointers for odd list
            odd.next = odd.next.next
            odd = odd.next

            # Change pointers for even list
            even.next = even.next.next
            even = even.next

        # Assign even list at the end of odd list
        odd.next = evenHead

        return head

s=Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Create an object of the Solution class
s = Solution()

# Rearrange the nodes in an odd-even pattern
new_head = s.oddEvenList(head)

# Output the modified linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")