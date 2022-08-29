import java.util.Scanner;
public class InsertionSort{
    public static void main(String[] args) {
        int length;
        Scanner read = new Scanner(System.in);
        length = read.nextInt();
        int[] arr = new int[length];
        for(int i=0; i<length; i++){
            arr[i] = read.nextInt();
        }
        for(int i=0;i<length-1;i++){
            for(int j=i+1;j<length;j++){
                if(arr[j]<arr[i]){
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        for(int i=0;i<length;i++){
            System.out.print(arr[i] + " ");
        }
        read.close();
    }
}