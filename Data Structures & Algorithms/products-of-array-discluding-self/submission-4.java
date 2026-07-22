class Solution {
    public int[] productExceptSelf(int[] nums) {
        int prefix = 1;
        int postfix = 1;
        int n = nums.length;
        int[] output = new int[n];

        for (int i = 0; i < n; i++) {
            output[i] = prefix;
            prefix *= nums[i];
        }

        for (int i = n - 1; i >= 0; i--) {
            output[i] *= postfix;
            postfix *= nums[i];
        }

        return output;
        
    }
}  
