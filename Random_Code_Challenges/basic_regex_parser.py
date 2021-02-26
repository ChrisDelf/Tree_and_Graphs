## Basic Regex Parser
##Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and pattern - and should return true if the text matches the pattern as a regular expression. For simplicity, assume that the actual symbols '.' and '*' do not appear in the text string and are used as special symbols only in the pattern string.

##In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.' is treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter (see fourth and fifth examples). For more information on regular expression matching, see the Regular Expression Wikipedia page.

##Explain your algorithm, and analyze its time and space complexities.


input_t1 = "aa"
input_p1 = "a"
## False

input_t2 = "aa"
input_p2 = "aa"
## True

input_t3 = "abc"
input_p3 = "a.c"
## True

input_t4 = "abbb"
input_p4 = "ab*"
## True

input_t5 = "acd"
input_p5 = "ab*c."
## False

def is_match(text, pattern):
  
  ## "." can be any letter
  ##"*"  can be a zero or more sequence
  if text == None or pattern == None:
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
  
  while pattern_1[pattern_pointer] != None or text_pointer <= len(text_1):
    character = ""
    pattern_character = ""
    symbol = ""
   ## grabing our character
    if text_pointer >= len(text_1):
      break

    if text_1[text_pointer] != None:
      character = text_1[text_pointer]
    else:
      break

  ## * is a special character we don't need it as a pattern_character
    if pattern_1[pattern_pointer] == "*":
      pattern_pointer += 1
    print("t_p", text_pointer, "p_p", pattern_pointer, " s_p", special_pointer)
  ## if we no longer have room for a symbol pointer aka special pointer then we ignore iter
    if special_pointer < len(pattern):
  ## see if there is pointer associated with the character
      if (pattern_1[special_pointer] != None) and (pattern_1[special_pointer] != "."):
       
        if pattern_1[special_pointer] == "*":
          symbol = "*"
        else:
          symbol = None
        
        ##if pattern_1[pattern_pointer] == "*":
       ##   pattern_pointer += 1
        pattern_character = pattern_1[pattern_pointer]
  ## if our pointer is equal to one of the special character we need to progress our pointers
      else:
        if pattern_1[pattern_pointer] == ".":
          symbol = None
          pattern_character = "."
        else:
          symbol = pattern_1[special_pointer]
          pattern_character = pattern_1[pattern_pointer]
  ## if our text character is equal to the character in the pattern and we are not dealing with an "*" do this
      print(character, pattern_character, symbol);
      if character ==  pattern_character and symbol != "*":
        ## this we will now progress all three pointers
        text_pointer += 1
        special_pointer += 1
        pattern_pointer += 1

      elif character !=  pattern_character and  pattern_character == ".":
        ## this we will now progress all three pointers
        text_pointer += 1
        special_pointer += 1
        pattern_pointer += 1
    ## the special case will be the "*"
      elif character !=  pattern_character and symbol == "*":
        ## this we will now progress all three pointers
        special_pointer += 2
        pattern_pointer += 2
        
     
      elif character ==  pattern_character and symbol == "*":
        ## now we must loop through the text string until we find the end
        text_pointer_copy = text_pointer
        for i in range(text_pointer, len(text_1)):
          text_pointer += 1
          print(text_pointer)
          if text_1[text_pointer_copy] != character:
            return False;
    else:
      
      pattern_character = pattern_1[pattern_pointer]
      print(pattern_character, character)
      if character == pattern_character or pattern_character == ".":
        text_pointer += 1
        special_pointer += 1
        pattern_pointer += 1
        
      else:
        return False
    
    if pattern_pointer >= len(pattern_1) and text_pointer >= len(text_1):
      break

    if pattern_pointer >= len(pattern_1):
      return False
      
    

  
    
  return True;
        
          

    
      
    
print(is_match(input_t5, input_p5))
