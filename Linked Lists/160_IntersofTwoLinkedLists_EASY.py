# Solved with TWO-POINTER & LINKED LIST
# Doesn't Run on VScode

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA, nodeB = headA, headB
        #find length of headA
        lenA = 0
        while nodeA:
            lenA += 1
            nodeA = nodeA.next

        #find length of headB
        lenB = 0
        while nodeB:
            lenB += 1
            nodeB = nodeB.next

        #diff length between two linked lists
        diff = abs(lenA - lenB)

        #traverse diff amount of steps of longer linked list
        #so that we will have same amount of nodes to traverse
        while diff:
            if lenA > lenB:
                while diff > 0:
                    headA = headA.next
                    diff -= 1
            else:
                while diff > 0:
                    headB = headB.next
                    diff -= 1

        #traverse both linked lists until the point of intersection
        #return the node where they intersect
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next