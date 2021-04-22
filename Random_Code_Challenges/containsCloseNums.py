def containsCloseNums(nums, k):
    ## we are checking the differences between one element to the next
    nums_dict = {}
    is_dup = False;
    result = True;
    for x in range(0,len(nums)):
        if nums[x] not in nums_dict:
            nums_dict[nums[x]] = x
        else:
            if x - nums_dict[nums[x]] > k:
                result = False;
            else:
                is_dup = True;
                result = True;
                break
            nums_dict[nums[x]] = x
            
    if is_dup == False:
        return False;
    return result;
