def climbStairs(self, n: int) -> int:
    #o(n) time complexity
    #o(1) memory

    one, two = 1, 1

    for i in range(n-1):
        temp = one
        one = one + two
        two = temp

    return one      
