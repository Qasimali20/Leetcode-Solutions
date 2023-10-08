class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Create an object of the Solution class
s1 = Solution()

# Delete the node with value 3
node_to_delete = head.next
s1.deleteNode(node_to_delete)

# Output the modified linked list: 1 -> 2 -> 4 -> 5
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")