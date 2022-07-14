def containsDuplicate(self, nums: List[int]) -> bool:
      #going to store the values in memory when iterating through the array
        number_store = {}
        isDup = False
        if len(nums) <= 0:
            return False

        for i in range(len(nums)):
            if nums[i] not in number_store:
                number_store[nums[i]] = 1
            else:
                number_store[nums[i]] += 1

    # going to need to do another iteration to go through the dictionary

        for key in number_store:
            value = number_store[key]
            if value > 1:
                isDup = True

        return isDup
