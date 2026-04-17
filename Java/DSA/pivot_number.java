class Solution {

    public int pivotInteger(int n) {
        int sum = (n * (n + 1)) / 2;
        int pivot = (int) Math.sqrt(sum);
        return pivot * pivot == sum ? pivot : -1;
    }
}

class pivot_number {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 12;
        int result = solution.pivotInteger(n);
        System.out.println(result);
    }
}
