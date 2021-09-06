boolean isBeautifulString(String inputString) {
    // creating a hasttable for our strings
    Hashtable<Character, Integer> letterHash = new Hashtable<Character, Integer>();
    int maxCount = 0;
    
    for (Character ch: inputString.toCharArray()){
      //  System.out.print("\n"+ch);
        


        if (letterHash.containsKey(ch) == false){
            letterHash.put(ch,0);
            
        }
        else{
          
            int tempN = letterHash.get(ch);
            tempN += 1;
            maxCount = tempN > maxCount ? maxCount = tempN : maxCount;
            letterHash.put(ch, tempN);
            
        }
        
    }
    
    // now that we have iterrate through our hash table we can check if any letters fall below the max
    //for (Map.Entry mapElement : letterHash.entrySet()){
    //    System.out.println(mapElement);
    //    int value = ((int)mapElement.getValue());
     //   if (value > maxCount){
     //       return false;
      //  }
        
    //}
    
    for (int i = 0; i < inputString.length(); i++) 
    {
        
    // going to need a prev, next pointer, current pointer
        char ch = inputString.charAt(i);       
        int prevPointer = i == 0 ? prevPointer = 0 : (prevPointer = i - 1);
        int nextPointer = (i+1) >= inputString.length() ? nextPointer = i : (nextPointer = i + 1);
        char prevChar = inputString.charAt(prevPointer);
        char nextChar = inputString.charAt(nextPointer);
        
        ///geting our values from our hashmap
        int nextValue = letterHash.get(nextChar);
        int prevValue = letterHash.get(prevChar);
        int currentValue = letterHash.get(ch);
        if (prevValue != currentValue)
        {
            return false;
            
        }
        if (nextValue != currentValue)
        {
            return false;
        }
        
      System.out.println(prevChar+" ,"+ ch + " ," +nextChar );
        
    // now since we have our pointers we can get our limits.
    
    }

    return true;

}
