class Solution {
    public int countDigits(int n) {
        
        //Recursive Approach
        
        // base case
        
        if(n/10 == 0)
            return 1;
        
        //recursion
        
        return 1 + countDigits(n/10);
    }
}
