boolean isMAC48Address(String inputString) {
    // want to do some checks to make sure we are dealing with a mac address
    if (inputString.length()!= 17)
    {
        
        return false;
    }
    //going to make a dictionary avaible letters
    Set<Character> stringSet = new HashSet<Character>();
    stringSet.add('A');
    stringSet.add('B');
    stringSet.add('C');
    stringSet.add('D');
    stringSet.add('E');
    stringSet.add('F');
    stringSet.add('1');
    stringSet.add('2');
    stringSet.add('3');
    stringSet.add('4');
    stringSet.add('5');
    stringSet.add('6');
    stringSet.add('7');
    stringSet.add('8');
    stringSet.add('9');
    stringSet.add('0');
    
    // now we need to iterate through the string;
    int dashCounter = 0;
    for (int i = 0; i < inputString.length(); i++) 
    {
        dashCounter += 1;
        if (stringSet.contains(inputString.charAt(i)) == false && dashCounter != 3)
        return false; 
    
    if (dashCounter == 3 && inputString.charAt(i) != '-')
    {
        return false;
    }
    else if (dashCounter == 3 && inputString.charAt(i) == '-')
    {
        dashCounter = 0;
    }

    }
    
   
     return true;
      

}
