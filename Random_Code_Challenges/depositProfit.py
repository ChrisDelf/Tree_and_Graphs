def depositProfit(deposit, rate, threshold):
 
    currentD = deposit
    yearC = 0
    currentR = rate / 100
    
    ## to get our decimal we can convert the rate into a string then into a float
    stringR = ""
    stringR += str(currentR)
    floatR = float(stringR)
    finalR = 1 + floatR
    while currentD < threshold:
        currentD = currentD * finalR
        yearC += 1
    
    return yearC
