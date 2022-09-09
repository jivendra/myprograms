import java.io.*;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner read = new Scanner(System.in);
        int rows = read.nextInt();
        int cols = read.nextInt();
        int[][] array = new int[rows][cols];
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                array[i][j] = read.nextInt();
            }
        }
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                System.out.print(array[i][j] + " ");
            }
            System.out.println("");
        }
        read.close();

    }
}
