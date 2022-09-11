import java.util.ArrayList;
import java.util.Collections;
public class ds_ArrayList {
    public static void main(String[] args) {

        //creation
        ArrayList<Integer> arr = new ArrayList<>();

        //adding elements
        arr.add(1);
        arr.add(4);
        arr.add(7);
        arr.add(1, 3);  //adding at a specific index
        System.out.println(arr.get(1));

        //update
        arr.set(1, 9);
        System.out.println(arr);

        //delete
        arr.remove(3);
        System.out.println(arr);

        //size of ArrayList
        System.out.println(arr.size());

        //iteration
        for(int i=0; i<arr.size(); i++){
            System.out.print(arr.get(i) + " ");
        }
        System.out.println();

        //sorting
        Collections.sort(arr);
        System.out.println(arr);
    }
}
