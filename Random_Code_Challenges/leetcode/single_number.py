def singleNumber(self, nums: List[int]) -> int:
    # going use a dictionary to store values
    n_hash = {}

    for i in range(len(nums)):
        if nums[i] not in n_hash:
            n_hash[nums[i]] = 1

        else:
            n_hash[nums[i]] += 1
    
    single = None
    for key in n_hash
        if n_hash[key] == 1:
            single = key
            return key

# solution 2
def singleNumber(self, nums: List[int]) -> int:
    res = 0
    for n in nums:
        res = n ^ res
    return res
