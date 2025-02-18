import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.

        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        String [] arr = s.split("\\.");
        String a = arr[0];
        String b = arr[1];
        String c = arr[2];

        System.out.println(b+"-"+c+"-"+a);
    }
}