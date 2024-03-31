import java.util.Scanner;

public class section2 {
	public static void main(String[] args) {
		
		Scanner scanIn = new Scanner(System.in);

        System.out.print("Enter three numbers: \n");
        int first_num = scanIn.nextInt();
        int gap = scanIn.nextInt();
        int size = scanIn.nextInt();         
        scanIn.close();
        
        if(size<0) {
        	System.out.print("Think about that !!\n");
        }
        
        for(int i=0; i<size; i++ ) {
        	System.out.print(i*gap+first_num+" ");
        }
        
		
	    
	}	
}

