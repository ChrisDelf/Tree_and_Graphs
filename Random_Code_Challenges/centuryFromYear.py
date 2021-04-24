def centuryFromYear(year):
    result = year / 100;
    mod = year % 100
    
    if mod == 0:
        return result
    else:
        return math.floor(result + 1)

