import java.util.Scanner;

public class LoginSystem {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        
        System.out.print("Enter your username: ");
        String username = input.nextLine();

        System.out.print("Enter your password: ");
        String password = input.nextLine();

      
        String admin = "adminKE";
        String passwordAdmin = "254Secure";

    
        if (username == admin && password == passwordAdmin) {
            System.out.println("Access granted!");
        } else {
            System.out.println("Invalid Credentials!");
        }

        input.close();
    }
}