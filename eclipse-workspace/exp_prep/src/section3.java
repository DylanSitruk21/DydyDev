import java.util.Random;


public class section3 {
	public static void main(String[] args) {

                           
	  Random rand = new Random();
	  int upperbound = 2;
	  int int_random = rand.nextInt(upperbound); 
	  
	  for (int j =0; j<3 ; j++) {
         for (int i = 0; i<3 ; i++) {
            int_random = rand.nextInt(upperbound); 
            System.out.print(int_random);
            System.out.printf(" ");
         
         }
         System.out.printf("\n");           
	  }
  }            
}
