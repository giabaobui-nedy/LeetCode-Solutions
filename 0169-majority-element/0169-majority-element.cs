
public class Solution {
    public int MajorityElement(int[] nums) {
       Dictionary<int, int> incidencesPerNum = new Dictionary<int, int>();

        foreach (int num in nums)
        {
            if (incidencesPerNum.ContainsKey(num))
            {
                incidencesPerNum[num] += 1;
            }
            else
            {
                incidencesPerNum.Add(num, 1);
            }
        }

        int maxValue = incidencesPerNum.Values.Max();

        foreach (KeyValuePair<int,int> pair in incidencesPerNum)
        {
            if (pair.Value == maxValue)
            {
                return pair.Key;
            }
        }

        return 0;
    }
}