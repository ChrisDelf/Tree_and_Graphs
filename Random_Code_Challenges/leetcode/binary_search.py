def search(self, nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] > target:
            return -1
        if nums[i] == target:
            return i

def search(self, nums: List[int], target: int) -> int:
    # the keyword for this search is that sorted array
    # going to use two pointers
    l,r = 0 , len(nums) -1 

    while l <= r:
        # since it is sorted we can find the midpoint and elminate half of our options
        m = (l+r) //2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        # the midpoint is our target
        else:
            return m
    return -1



