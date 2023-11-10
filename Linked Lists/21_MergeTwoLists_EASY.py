#LeetCode 21
# Linked Lists

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        head = dummyNode
    
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next
	
				#checking if either lists have some nodes left
        if list1:
            head.next = list1
        
        if list2:
            head.next = list2

        return dummyNode.next