class Solution {
    public int countDigits(int n) {
        
        //Logarithmic Approach
        
        //base case
        
        if (n == 0)
            return 1;
        
        return (int)Math.floor(Math.log10(n)+1);
        
    }
}
