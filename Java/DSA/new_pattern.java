public class new_pattern {

    public static void main(String[] args) {
        new_pattern p1 = new new_pattern();
        int rows = 5;
        p1.drawDiamond(rows);
    }

    public void drawDiamond(int n) {
        // Forward (Upper Pyramid)
        for (int i = 1; i <= n; i++) {
            printLine(n, i);
        }
        // Backward (Lower Inverted Pyramid)
        for (int i = n - 1; i >= 1; i--) {
            printLine(n, i);
        }
    }

    private void printLine(int totalRows, int currentRow) {
        // Print leading spaces
        for (int s = 1; s <= totalRows - currentRow; s++) {
            System.out.print(" ");
        }
        // Print stars with a trailing space for a clean equilateral look
        for (int k = 1; k <= currentRow; k++) {
            System.out.print("* ");
        }
        System.out.println();
    }
}
