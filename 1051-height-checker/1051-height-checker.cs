public class Solution {
    public int HeightChecker(int[] heights) {
        int[] expecteds = new int[heights.Length];
        heights.CopyTo(expecteds, 0);
        Sort(expecteds, 0, expecteds.Count() - 1);
        int timesNotMatch = 0;
        for (int i = 0; i< heights.Length; i++) {
            if (heights[i] != expecteds[i]) {
                timesNotMatch++;
            }
        }
        return timesNotMatch;
    }
    
    private static void Sort(int[] arr, int left, int right)
        {
            if (left < right)
            {
                int pivot = Partition(arr, left, right);
                Sort(arr, left, pivot - 1);
                Sort(arr, pivot + 1, right);
            }
        }
    
    private static int Partition(int[] arr, int left, int right)
    {
        int pivot = arr[right];
        int i = left - 1;
        for (int j = left; j < right; j++)
        {
            if (arr[j] <= pivot)
            {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp1 = arr[i + 1];
        arr[i + 1] = arr[right];
        arr[right] = temp1;
        return i + 1;
    }
}