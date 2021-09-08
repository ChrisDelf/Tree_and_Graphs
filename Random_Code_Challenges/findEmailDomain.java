String findEmailDomain(String address) {
    String resultString = "";
    boolean isDomain = false;

    for(int i = 0; i < address.length(); i ++)
    {   
       char ch = address.charAt(i);
        if (isDomain == true && ch != '@')
        {
 
            resultString = resultString + ch;
        }
        else if (isDomain == true && ch == '@')
        {
            resultString = "";
        }
   
        if (ch == '@' && isDomain == false)
        {
        // going to have a condition the state that we are currenty iterating through a potetional address
            
            isDomain = true;
            System.out.println(isDomain);
        }
        
    }
    return resultString;
}

