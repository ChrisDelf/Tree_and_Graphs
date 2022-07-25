#solution #1
def hammingWeight(self, n: int) -> int:
    counter = 0

    while n:
        counter += n % 2
        n = n >> 1
    return counter
#solution 2
def hammingWeight(self, n: int) -> int:
    res = 0
    while n:
        n &= n - 1
        res += 1
    return res
