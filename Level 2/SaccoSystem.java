import java.util.Scanner;

public class SaccoSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter Member Name: ");
        String memberName = scanner.nextLine();

        System.out.print("Enter Member ID: ");
        int memberID = scanner.nextInt();

        double[] contributions = new double[6]; // Fixed-size Composite Type
        double totalSavings = 0;

        for (int i = 0; i < 6; i++) {
            System.out.print("Month " + (i + 1) + " contribution: ");
            contributions[i] = scanner.nextDouble();
            totalSavings += contributions[i];
        }

        System.out.println("\nMember: " + memberName + " (ID: " + memberID + ")");
        System.out.println("Total Savings: KES " + totalSavings);
    }
}