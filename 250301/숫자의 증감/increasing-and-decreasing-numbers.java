import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        char x = sc.next().charAt(0);
        int k = sc.nextInt();

        if ( x=='A'){
            for(int i=1;i<=k;i++){
                System.out.printf("%d ",i);
            }

        }else{
            for(int i=k;i>0;i--){
                System.out.printf("%d ",i);
            }
        }
    }
}