import java.util.Scanner;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.

        Scanner sc= new Scanner(System.in);

        List<Integer> a = Arrays.asList(1, 3, 5, 7, 8, 10, 12);
        // 30일이 있는 달
        List<Integer> b = Arrays.asList(4, 6, 9, 11);


        int k = sc.nextInt();

        if (a.contains(k)){
            System.out.println(31);
        }
        else if(b.contains(k)){
            System.out.println(30);
        }
        else{
            System.out.println(28);
        }
    }
}