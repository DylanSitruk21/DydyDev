import java.util.Scanner;

public class section1 {
	public static void main(String[] args) {
		System.out.println("Enter a number: ");
		
		Scanner scanIn = new Scanner(System.in);
		int num = scanIn.nextInt();
		scanIn.close();            
		
		if(num<0) {
	        System.out.print("Think about that !!\n");
	    }
		
		for (int i = 0; i<num ; i++) {
			String space = String.format("%"+ (i+1) +"s"+"%n", "*");
			System.out.printf(space);
		}
	    
	}	
}