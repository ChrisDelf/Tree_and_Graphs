String buildPalindrome(String st) {

        String rs = new StringBuffer(st).reverse().toString();

        for (int i = 0; i < st.length(); i++) {
			
		if (rs.startsWith(st.substring(i))) {

			return st.substring(0, i) + rs;
		}
	}
		
	return "?";
}

