def containsCloseNums(nums, k):
    ## we are checking the differences between one element to the next
    nums_dict = {}
    # for x in range(0,len(nums)):
    #     if nums[x] not in nums_dict:
    #         nums_dict[nums[x]] = 0
    #     else:
    #         nums_dict[nums[x]] += 1
    counter = 0
    is_dup = False
    result = False
    for i in range(0, len(nums)):
        ## when we move to the next index we reset the coutner
        counter = 0
        for j in range(i+1,len(nums)):
            ## now we iterrate through the rest of the array to and if there is a dup
            counter += 1
            if nums[i] == nums[j]:
                is_dup = True;
                if counter > k:
                    break
                else:
                    result = True;
                    break
        
    if is_dup == False:
        return result;
    else:
        return result;
