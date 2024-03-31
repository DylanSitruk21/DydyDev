import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.Socket;

public class client {
	  public static void main(String[] args) {  
		  try{      
			  Socket soc=new Socket("localhost",12345);  
			  DataOutputStream out=new DataOutputStream(soc.getOutputStream());  
			  DataInputStream in = new DataInputStream(soc.getInputStream());
			  String msg=(String)in.readUTF();
			  System.out.println("Server: "+msg);
			  System.out.println("Write your message: ");
			  BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));
		      String answer = bufferRead.readLine();
			  out.writeUTF(answer);
			  out.flush();
			  out.close();
			  soc.close();
		  }
		  catch(Exception e)
		  {
			  e.printStackTrace(); 
		  }
	}
}