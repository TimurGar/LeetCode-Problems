
# ! Remember !
# O(n)

# Creating two linked list for odd and even nodes
def oddEvenList(head):
    # if list is empty
    if head is None:
        return None
    
    odd = head
    # dummyNode is to keep the location of the even head
    # bec we will need it to attach two lists together
    dummyNode = even = head.next
    
    while even and even.next:
        # Jumping over a node to get the next odd, and setting the 
        # pointer of odd node to point to another odd node
        odd.next = odd.next.next
        # Same for even
        even.next = even.next.next

        # Moving the start location to the next odd node 
        # (that we attached in the previous step)
        odd = odd.next
        # Same for even
        even = even.next
    
    # Combinig the two lists into one
    odd.next = dummyNode
    return head   