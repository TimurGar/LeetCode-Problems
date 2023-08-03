
# Floyd's Tortoise and Hare
# Solved with TWO-POINTER & LINKED LIST
# O(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        # making sure that fast and fast.next is Not equal to NUll
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

             
            if slow == fast:
                return True
            
        return False
    
test1 = Solution()
test1.hasCycle(head = [3,2,0,-4])