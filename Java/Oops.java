import java.util.Scanner;
import java.io.*;
public class Oops {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in) ;
		if (System.getProperty("ONLINE_JUDGE") == null) {

			try {
				System.setOut(new PrintStream(new FileOutputStream("output.txt")));
				in = new Scanner(new File("input.txt"));
			}
			catch (Exception e) {
			}
		}
        
        

        in.close();
    }
}