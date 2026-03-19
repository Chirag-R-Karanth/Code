import java.util.Scanner;

public class Pythagorean_triplets {

    public static void main(String[] args) {
        int[] triple = new int[3];
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 3; i++) {
            triple[i] = sc.nextInt();
        }
        Pythagorean_triplets obj1 = new Pythagorean_triplets();
        triple = obj1.sorting(triple); // pass to sorting, get back sorted array
        obj1.calc(triple); // pass sorted array to calc
        //return obj1.calc(triple) ? 1 : 0;
    }

    public int[] sorting(int[] triple) {
        // write your own sorting logic here (bubble sort, selection sort, etc.)
        // example structure for bubble sort:
        for (int i = 0; i < triple.length - 1; i++) {
            for (int j = 0; j < triple.length - i - 1; j++) {
                if (triple[j] > triple[j + 1]) {
                    if (triple[j] > triple[j + 1]) {
                        triple[j] += triple[j + 1];
                        triple[j + 1] = triple[j] - triple[j + 1]; // ← this line is different
                        triple[j] -= triple[j + 1];
                    }
                }
            }
        }
        return triple;
    }

    public boolean calc(int[] triple) {
        int a = triple[0],
            b = triple[1],
            c = triple[2];
        if (c * c == a * a + b * b) {
            System.out.println("yes");
            return true;
        } else {
            System.out.println("no");
            return false;
        }
    }
}
