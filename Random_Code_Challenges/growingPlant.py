def growingPlant(upSpeed, downSpeed, desiredHeight):
    plantH = 0
    days = 0
    
    while plantH <= desiredHeight:
        ## daytime
        plantH += upSpeed
        if plantH >= desiredHeight:
            days += 1
            return days
        ##nighttime
        plantH -= downSpeed
        
        days += 1
        
        
    return days
