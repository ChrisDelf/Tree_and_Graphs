def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #going to need a dummy node to prevent edge cases
    dummyN = ListNode()
    tail = dummyN
    l1 = list1
    l2 = list2
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1 != None:
        tail.next = l1
    if l2 != None:
        tail.next = l2
    
    return dummyN.next
