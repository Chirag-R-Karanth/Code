class AP {

    public boolean canMakeArithmeticProgression(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = arr.length - 1; j > i; j--) {
                if (arr[j - 1] > arr[j]) {
                    arr[j] = arr[j - 1] + arr[j];
                    arr[j - 1] = arr[j] - arr[j - 1];
                    arr[j] = arr[j] - arr[j - 1];
                }
            }
            System.out.println(arr[i]);
        }

        for (int i = 0; i <= arr.length - 3; i++) {
            if (arr[i + 1] - arr[i] != arr[i + 2] - arr[i + 1]) {
                System.out.println("false");
                return false;
                //exit(0);
            }
        }
        System.out.println("true");
        return true;
    }

    public static void main(String[] args) {
        AP sort = new AP();
        sort.canMakeArithmeticProgression(
            new int[] {
                -509,
                -19,
                -439,
                -264,
                -404,
                -369,
                -299,
                -89,
                -229,
                -54,
                -194,
                +16,
                -544,
                -159,
                -124,
                -474,
                -334,
            }
        );
    }
}
