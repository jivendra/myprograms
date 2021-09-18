//Problem link - https://www.hackerrank.com/challenges/java-loops/problem
import java.io.*;
import java.util.*;
public class Java_loops_2{
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        int q,a,b,n;
        q=obj.nextInt();
        while(q!=0){
            a=obj.nextInt();
            b=obj.nextInt();
            n=obj.nextInt();
            for(int i=0;i<n;i++){
                int ans = a;
                for(int j=0;j<=i;j++){
                    ans+=b*(int)Math.pow(2,j);
                }
                System.out.print(ans + " "); 
            }
            System.out.println(" ");
            q--;
        }
        obj.close();
    }
}
