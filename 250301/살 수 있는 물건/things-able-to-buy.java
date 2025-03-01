import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int money = sc.nextInt();

        if (money>=3000){
            System.out.println("book");
            // break;
        }else if(money>=1000){
            System.out.println("mask");
            // break;
        }else{
            System.out.println("no");
        }

    }
}