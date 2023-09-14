# Array and O(1) memory Solutions
def isPalindrome(head):
    # Most optimal solution

    slow, fast = head, head

    # finding the middle of the linked list 
    # (slow pointer will point to the middle)
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Switiching (reversing) the pointers on the second half of the linked list
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # Checking if it's a palindrome

    # right is set to prev bec, slow will be None after 
    # the while but prev will point to the last element
    left, right = head, prev
    # None <- 2 <- 1 - second half 
    while right:
        if left.val != right.val:
            return False
        
        left = left.next
        right = right.next

    return True


    # Array solution
    # arr = []

    # curr = head
    # while curr:
    #     arr.append(curr.val)
    #     curr = curr.next

    # front, back = 0, len(arr)-1

    # while back > front:
    #     if arr[front] != arr[back]:
    #         return False
    #     back -= 1
    #     front += 1

    # return True 

