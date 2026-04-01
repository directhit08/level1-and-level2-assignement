import java.util.Scanner;

public class DroughtAdvisory {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter rainfall amount (mm): ");
        double rainfall = scanner.nextDouble();

        System.out.print("Enter temperature (°C): ");
        double temperature = scanner.nextDouble();

        
        if (rainfall < 200) {
            System.out.println("Advisory: Irrigation Required");
        } else if (rainfall >= 200 && temperature > 30) {
            System.out.println("Advisory: Monitor Soil");
        } else {
            System.out.println("Advisory: Normal Conditions");
        }
        
        scanner.close();
    }
}