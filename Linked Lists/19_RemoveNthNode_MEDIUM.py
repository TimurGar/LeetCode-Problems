# Solved with TWO-POINTER & LINKED LIST
# 0(n)

# Mine worked but it was slow

# Notes
# keep track of prev node, curr
# iterate through to find length, then substact n to get the index of the element to remove
# iterate, updating the curr, and prev
# when curr is the nodeToRemove,(don't update the prevNode) go one futher, and then set prevNode.next to curr

def removeNthFromEnd(head, n):
    # Creating a dummy node to put in front of the head, to make sure
    # that left will actually be one node behing the NodeToRemove, when right reaches the end
    # this is so that we can remove the required NodeToRemove
    dummyNode = ListNode(0, head)
    left = dummyNode
    right = head
    
    # Setting right to be n nodes apart 
    # Ex: n = 2(1 -> 2 -> 3) (left = 1, right = 3)
    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next
    
    # Deleting the NodeToRemove
    left.next = left.next.next

    return dummyNode.next
    

    # My code
    # currNode, prevNode = head, head
    # length = 0
    # iElementToRemove = 0
    
    # # finding the length
    # while currNode:
    #     length += 1
    #     currNode = currNode.next

    # if length == 1:
    #     head = None
    #     return
    
    # iElementToRemove = length - n

    # if iElementToRemove == 0:
    #     return head.next

    # currNode = head

    # # iterating to an element that needs to be removed
    # for i in range(iElementToRemove):
    #     prevNode = currNode
    #     currNode = currNode.next
        
    # # currNode - nodeToRemove.next
    # currNode = currNode.next

    # prevNode.next = currNode

    # return head
