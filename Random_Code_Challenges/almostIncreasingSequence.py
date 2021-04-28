def almostIncreasingSequence(sequence):
    # need a dictionary to check for dups
    dups = {}

    # we are going to iterrate through the array
    current = 0
    counter = 0
    ## this pointer is going to compare the next index and if it encounter a removal then it will trigger a check iterration
    next_p = 0
    
    ## we are we need something the check for the lowest number in our sequence 
    lowest_s = None
    
    for i in range(0 , len(sequence)):
        current = sequence[i]
        start = i + 1
        if i + 1 >= len(sequence):
            next_p = None
        else:
            next_p = sequence[i+1]
            
        if lowest_s == None:
            lowest_s = current
            ## we need to check if the first index is the lowest number
            if next_p != None and lowest_s > next_p:
               lowest_s = next_p
            
            
        
            
        
        if current not in dups:
            dups[current] = 0
        else:
            dups[current] += 1
        
        ## we have encounter a removal instance
 
        if next_p != None and current > next_p:
            ## going to save the value of the counter to compare after the iterration to see if we ran into any of the conditions if not we know to remove the current index to reslove the issue:
            saved_counter = counter
            for j in range(start, len(sequence)):
                if sequence[j] <= lowest_s:
                    counter += 1
            ## here we make the comparison mention in previous comment:
            if saved_counter == counter:
                counter += 1
    d_counter = 0
    for key in dups:
        d_counter += dups.get(key)
    print(d_counter)
    if counter != d_counter and counter + d_counter > 1:
        return False
    else:
        return True
