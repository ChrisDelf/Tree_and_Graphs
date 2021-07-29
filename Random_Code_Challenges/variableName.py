def variableName(name):
    ## going to have to convert this form a string into an array
    
    englishArray = []
    counter = 0
    for char in name:
        if char.isalpha() == True:
            englishArray.append(char)
        elif char.isnumeric() == True:
            if counter == 0:
                return False
            englishArray.append(int(char))
        elif char == "_":
            englishArray.append(char)
        else:
            return False
        counter += 1
    return True
