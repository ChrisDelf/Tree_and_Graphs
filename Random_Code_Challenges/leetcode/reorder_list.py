def reorderList(self, head: Optional[ListNode]) -> None:
    #going to use two pointers
    slow, fast = head, head.next
    
    # while fast has not reach the end of the list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    #this will be the start of the second half of the list
    second = slow.next
    # before we split the list we want to set the 
    # end of the first half of the list to null
    slow.next = None
    prev = None
    #reversing the second half of the list
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp
    #merging the two list
    second = prev
    first = head

    while second:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        # now we shift our pointers
        first = temp1
        second = temp2
        




