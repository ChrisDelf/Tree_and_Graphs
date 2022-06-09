# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        current1 = l1
        last1 = l1
        head1 = l1
        currentS1 = ""
        
        current2 = l2
        last2= l2
        head2 = l2
        currentS2 = ""
        
        resultLN = None
        currentResult = None
        prevLN = None
        
        
        while current1 or current2:
            #going result to a corresponding lists
            
            if current1 != None:
                currentS1 = str(current1.val) + currentS1
                current1 = current1.next
            if current2 != None:
                currentS2 = str(current2.val) + currentS2
                current2 = current2.next
           
            
            
        
        ## now that we have our string we can now convert back into ints and add them together
       
        the_sum = int(currentS1) + int(currentS2)
        ## now we can create our new linked list
        for x in reversed(str(the_sum)):
            if resultLN == None:
                
                resultLN = ListNode(int(x), None)
                resultHead = resultLN
                currentLN = resultLN
                prevLN = currentLN
            else:
                if currentLN != None:
                    nextLN = ListNode(int(x), None)
                    prevLN.next = nextLN 
                    prevLN = prevLN.next 
                   

        return resultLN
            
