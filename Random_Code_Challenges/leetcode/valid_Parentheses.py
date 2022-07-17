def isValid(self, s: str) -> bool:
    # going to stack 
    stack = []
    # going to store values is a hashmap
    close_open_pare = {"]": "[" , ")": "(", "}" : "{"}
    
    for c in s:
        if c in close_open_pare:
            #we cannont add a closing parenthese to our stack
            # also i must match to its opening bracket
            if stack and stack[-1] == close_open_pare[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    if len(stack) == 0:
        return True
    else:
        return False


               

