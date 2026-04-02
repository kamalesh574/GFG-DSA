class Solution {
    public int countDigits(int n) {
        int count = 0;
        n = Math.abs(n);
        while (n > 0) {
            count++;
            n /= 10;
        }
        return count == 0 ? 1 : count;
    }
}
