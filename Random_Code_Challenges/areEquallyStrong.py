def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    ## going to use a dictionary
    
    armArray = []
    
    yourArms = {}
    yourArms["right"] = yourRight
    yourArms["left"] = yourLeft
    
    friendsArms = {}
    friendsArms["right"] = friendsRight
    friendsArms["left"] = friendsLeft
    
    armStrength = 0
    
    for key in yourArms:
        for arm in friendsArms:
            if yourArms[key] == friendsArms[arm]:
                yourArms[key] -= friendsArms[arm] 
    
    for key in yourArms:
        armStrength += yourArms[key]

    if armStrength == 0:
        return True
    else:
        return False    
    
        
    
