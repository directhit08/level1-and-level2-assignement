public class AccessControl {
    public static void checkAccess(String role) {
        if (!role.equals("Doctor")) {
            throw new SecurityException("Access Denied: Unauthorized Role.");
        }
        System.out.println("Access Granted.");
    }

    public static void main(String[] args) {
        try {
            checkAccess("Patient");
        } catch (SecurityException e) {
            System.out.println("Caught Error: " + e.getMessage());
        }
    }
}