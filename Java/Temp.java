import java.util.Arrays;
import java.util.Scanner;
import java.io.*;
public class Temp {
    public static void main(String[] args) {
        // File I/O
        Scanner in = new Scanner(System.in) ;
		if (System.getProperty("ONLINE_JUDGE") == null) {

			try {
				System.setOut(new PrintStream(new FileOutputStream("output.txt")));
				in = new Scanner(new File("input.txt"));
			}
			catch (Exception e) {
			}
		}
        // Code below

        int[] arr = {10, 11, 12, 13, 14};
        int pos = 2;
        int element = 32;
        for(int i=arr.length-1;i>=pos;i--){
            arr[i] = arr[i-1];
        }
        arr[pos-1] = element;
        System.out.println(Arrays.toString(arr));
        
        String name = "Jivendra";
        System.out.println(name);
        System.out.println(name.lastIndexOf("end"));
        System.out.println(Arrays.toString(name.toLowerCase().toCharArray()));
        String name2 = "Jivendra";
        System.out.println(name == (name2));
        in.close();
    }
}