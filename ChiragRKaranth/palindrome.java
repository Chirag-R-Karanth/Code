import java.util.Scanner;

class Palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        
        // Check for valid integer input
        if (!sc.hasNextInt()) {
            System.out.println("Invalid input. Please enter an integer.");
            sc.close();
            return;
        }
        
        int num = sc.nextInt();
        sc.close();
        
        // Test both methods
        if (palindromeWithString(num)) {
            System.out.println("Palindrome (using string method)");
        } else {
            System.out.println("Not Palindrome (using string method)");
        }
        
        palindromeWithoutString(num);
    }

    // Method to check palindrome using String
    public static boolean palindromeWithString(int num) {
        // Handle negative numbers (not palindromes)
        if (num < 0) {
            return false;
        }
        String original = String.valueOf(num);
        StringBuilder reversed = new StringBuilder();
        int length = original.length();
        
        // Build reversed string
        while (length > 0) {
            reversed.append(original.charAt(length - 1));
            length--;
        }
        
        return original.equals(reversed.toString());
    }

    // Method to check palindrome without using String
    public static void palindromeWithoutString(int num) {
        // Handle negative numbers
        if (num < 0) {
            System.out.println("Not Palindrome (negative numbers are not palindromes)");
            return;
        }
        
        int original = num;
        int reversed = 0;
        
        // Reverse the number
        while (num != 0) {
            int digit = num % 10; // Get the last digit
            reversed = reversed * 10 + digit; // Build reversed number
            num = num / 10; // Remove the last digit
        }
        
        // Check if original number equals reversed number
        if (original == reversed) {
            System.out.println("Palindrome (using numeric method)");
        } else {
            System.out.println("Not Palindrome (using numeric method)");
        }
    }
}