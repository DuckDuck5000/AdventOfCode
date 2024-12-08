import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        List<Integer> depths = new ArrayList<Integer>();
        depths = init();

       
        int[] positiveChanges = day1(depths);
        System.out.println("Part One: " + positiveChanges[1]);
        System.out.println("Part Two: " + positiveChanges[0]);

    }

    /**
     * creates a list, to which it adds all numbers from the file
     * @return a list with all numbers
     */
    public static List<Integer> init() {
        List<Integer> list = new ArrayList<Integer>();        
        try {
            FileInputStream file = new FileInputStream("input.txt");
            Scanner sc = new Scanner(file);
            while(sc.hasNextLine()) {
                list.add(Integer.parseInt(sc.nextLine()));
            }
            sc.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return list;
    }

    /**
     * counts the times where the following number is greater then the number before
     * @param list contains all the numbers
     * @return the number times the measurement increases
     */
    public static int[] day1(List<Integer> list) {
        int n = 0;
        int m = 0;
        for (int i = 0; i < list.size(); i++){
          if ( i >= 1 && list.get(i) > list.get(i-1)){
              n++;
          }
          if (i >= 3){
            int firstSum = list.get(i-1) + list.get(i-2) + list.get(i-3);
            int secondSum = list.get(i) + list.get(i-1) + list.get(i-2);
            if (secondSum > firstSum){
              m++;
            }
          }
        }

        int[] arr = {m, n};
        return arr;
    }
}
