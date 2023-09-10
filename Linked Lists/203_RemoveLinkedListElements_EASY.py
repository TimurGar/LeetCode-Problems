# ! Remember !
# Check NeetCode video if needed 

# T O(n), M: O(1)
def removeElements(head, val): 
    # Creating a dummy node to easily deal with edge cases
    # As dummyNode.next always points to the head of linkedlist
    # useful when we want to remove the first element
    dummyNode = ListNode(next=head)
    prev, curr = dummyNode, head

    while curr:
        nxt = curr.next

        if curr.val == val:
            # removing the element
            prev.next = nxt
        else:
            prev = curr
        
        curr = curr.next

    return dummyNode.next

        