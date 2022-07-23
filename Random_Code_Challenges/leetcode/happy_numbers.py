def isHappy(self, n: int) -> bool:
    #we are going to convert the n into a string to 
    # grab the individual digits
    # going to create a while loop
    # while len(n) > 0:
    # going to use a hashset to save the result to stop when 
    # finding a dup

    visit = set()

    while n not in visit:
        visit.add(n)
        n = self.sumOfSquares(n)
        
        if n == 1:
            return True
    return False


def sumOfSquares(self, n: int) -> int:
    output = 0

    while n:
        digit = n % 10
        # double staring is how we square in python
        digit = digit ** 2
        output += digit
        n = n // 10
    return output
