# ! Remember !
# Check NeetCode video if needed 

# Iterative way 
# T O(n), M: O(1)
def reverseList(head):
    # ! initially the prev is Null
    curr, prev = head, None

    while curr:
        # temp var to not lose the curr.next (as we need it to later update the curr)
        nxt = curr.next

        # reversing the arrows
        curr.next = prev

        # moving the pointers
        prev = curr
        curr = nxt
        
    return prev