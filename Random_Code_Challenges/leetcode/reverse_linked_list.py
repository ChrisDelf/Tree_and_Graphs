def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #going to use two pointers
    previous, current = None , head


    while current != None:
        # going to save the next pointer for later
        temp = current.next
        # changing reversing the pointer
        current.next = previous
        #moving to the both of the pointers
        previous = current
        #using the temp value to move the current pointer
        current = temp

    return previous

def reverseListRec(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # recursive:
        if not head:
            return None
    # going to need to store the head value
    new_head = head

    if head.next:
        self.reversListRec(head.next)
        head.next.next = head
    head.next = next

    return new_head
