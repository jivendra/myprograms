package javaLanguage;

import java.util.Scanner;
public class Input {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a number : ");
        int number = input.nextInt();
        System.out.println("You entered " + number);
        System.out.print("Enter a line : ");
        String line = input.nextLine();
        System.out.println(line);
        System.out.println(Math.max(5,7));
    }
}
