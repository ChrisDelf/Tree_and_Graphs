def is_match(text, pattern):
  ## "." can be any letter
  ##"*"  can be a zero or more sequence
  if text == None or pattern == None
    return False
  ## we could use two pointer as we itterate through the text
  text_1 = text
  pattern_1 = pattern
  text_pointer = 0
  special_pointer = 1
  pattern_pointer = 0
  
  character = ""
  symbol = ""
  special_characters = [".","*"]
  
  while pattern_1[pattern_pointer] != None
    character = ""
    ## if our symbol is a * this is a very special case and we have to halt some pointers
    if symbol != "*":
      symbol = ""
    else:
      special_pointer
   ## grabing our character
    if text_1[text_pointer] != None:
      character = text_1[text_pointer]
    else:
      break
  ## see if there is pointer associated with the character
    if pattern_1[special_pointer] != None:
      for x in special_characters:
        if pattern_1[special_pointer] == x:
          symbol = x
  ## if our text character is equal to the character in the pattern and we are not dealing with an "*" do this
    if character == pattern_1[pattern_pointer] && symbol != "*":
      
      
      ## this we will now progress all three pointers
      
      text_pointer += 1
      special_pointer += 1
      pattern_pointer += 1
    
    else if character != pattern_1[pattern_pointer] && symbol == "."
      ## this we will now progress all three pointers
      text_pointer += 1
      special_pointer += 1
      pattern_pointer += 1
   ## the special case will be the "*"
    else if character != pattern_1[pattern_pointer] && symbol == "*";
      ## this we will now progress all three pointers
      text_pointer += 1
      special_pointer += 1
      pattern_pointer += 1
    else if character == pattern_1[pattern_pointer] && symbol == "*";
