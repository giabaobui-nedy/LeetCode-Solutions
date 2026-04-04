class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int searchedIndex;
        int searchedValue;
        while (left <= right) {
            searchedIndex = (left + right) / 2;
            searchedValue = nums[searchedIndex];
            if (searchedValue == target) {
                return searchedIndex;
            } else if (searchedValue > target) {
                right = searchedIndex - 1;
            } else {
                left = searchedIndex + 1;
            }
        }

        return -1;
    }
}