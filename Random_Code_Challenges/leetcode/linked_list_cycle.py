def hasCycle(self, head: Optional[ListNode]) -> bool:
    # this the time complexity is going to be O(n)
    # since we are going to use a hashmap to save the nodes memory complexity
    #will be O(n) aswell
    current = head
    node_hash = {}
    while current:
        if current not in node_hash:
            node_hash[current] = 0
        else:
            return True
        current = current.next

    return False

def hasCycleTurtleAndHair(self, head: Optional[listNode]) -> bool:
    # This solution requires two pointers
    # time complexity O(n) and memory O(n)
    # going to need a slow and fast pointer
    slow, fast = head, head
    
    #going to need to check for fast.next is null aswell
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True


    return False

