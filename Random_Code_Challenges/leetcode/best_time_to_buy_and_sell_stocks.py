def maxProfit(self, prices: List[int]) -> int:
    #going to use two pointer solution
    #time complexity is going to be O(n) memory is going to be o(1)

    #left and right pointers
    l, r = 0, 1 # left is buy right is sell
    max_P = 0

    while r < len(prices):
        # want to check the difference to see if profitable
        profit = prices[r] - prices[l]

        if prices[l] < prices[r]:
            max_P = max(max_P, profit)
        else:
            # we want to shift the buy pointer all the way to the new lowest price
            l = r
        r += 1

    return max_P
