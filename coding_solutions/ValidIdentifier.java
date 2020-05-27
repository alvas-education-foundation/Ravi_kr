// Java program to validate the identifiers using Regular Expression. 

import java.util.regex.*; 

class GFG { 

	// Function to validate the identifier. 
	public static boolean
	isValidIdentifier(String identifier) 
	{ 

		// Regex to check valid identifier. 
		String regex = "^([a-zA-Z_$][a-zA-Z\\d_$]*)$"; 

		// Compile the ReGex 
		Pattern p = Pattern.compile(regex); 

		// If the identifier is empty 
		// return false 
		if (identifier == null) { 
			return false; 
		} 

		// Pattern class contains matcher() method 
		// to find matching between given identifier 
		// and regular expression. 
		Matcher m = p.matcher(identifier); 

		// Return if the identifier 
		// matched the ReGex 
		return m.matches(); 
	} 

	// Driver Code. 
	public static void main(String args[]) 
	{ 

		// Test Case 1: 
		String str1 = "$valid123"; 
		System.out.println(isValidIdentifier(str1)); 

		// Test Case 2: 
		String str2 = "$hell ks123"; 
		System.out.println(isValidIdentifier(str2)); 

		// Test Case 3: 
		String str3 = "1hello$"; 
		System.out.println(isValidIdentifier(str3)); 
	} 
}
