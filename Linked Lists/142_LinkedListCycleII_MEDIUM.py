# Floyd's Tortoise and Hare
# Solved with TWO-POINTER & LINKED LIST
# Doesn't Run on VScode
# O(n)
# Excellent explanation of why the second part works (iterating by 1):
# https://www.youtube.com/watch?v=wjYnzkAhcNk&t=392s&ab_channel=NeetCode

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow == fast:
            # If the pointers meet, there is a cycle in the linked list.
            # Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
            # until they meet again. The node where they meet is the starting point of the cycle.
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow

        return None
    