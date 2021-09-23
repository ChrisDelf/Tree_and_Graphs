String lineEncoding(String s) {
    Matcher m = Pattern.compile("([a-z])\\1*").matcher(s);
    String result = "";
    while(m.find()){
        int len = m.group(0).length();
        char cha = m.group(0).charAt(0);
        result += (len==1?"":len) + "" + cha;
    }
    return result;
}
