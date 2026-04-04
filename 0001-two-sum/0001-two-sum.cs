public class Solution {
    
    public int[] TwoSum(int[] nums, int target) {
        int currentIndex = 0;
        int comparedIndex;

        //check if the pointer has reached the end of the list
        while (currentIndex < nums.Length)
        {
            comparedIndex = nums.Length - 1;
            // only compare later values (greater index)
            while (currentIndex < comparedIndex)
            {
            
                if (nums[currentIndex] + nums[comparedIndex] == target)
                {
                    return new int[] { currentIndex, comparedIndex };
                }
                comparedIndex -= 1;
            }
            currentIndex += 1;
        }
        return new int[] { 0, 0 };
    }
}