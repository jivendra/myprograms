package javaLanguage;
import java.util.Scanner;
public class Sum {
    public static void main(String[] args) {
        int num1, num2;
        System.out.print("Enter number 1 : ");
        Scanner in = new Scanner(System.in);
        num1 = in.nextInt();
        System.out.print("Enter number 2 : ");
        num2 = in.nextInt();
        System.out.println(addition(num1, num2));

    }

    static int addition(int a, int b) {
        return a+b;
    }
}
