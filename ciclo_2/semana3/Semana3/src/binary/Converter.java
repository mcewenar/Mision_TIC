package binary;

public class Converter {
	public static String toBinary(int num) {
		String binary="";
	    while(num > 0) {
	    	binary = (num%2)+binary;
	        num /= 2;
	    }
	    return binary;
	}
}
