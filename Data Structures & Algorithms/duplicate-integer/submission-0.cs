public class Solution {
    public bool hasDuplicate(int[] nums) {
        var seen_numbers = new HashSet<int>();
        foreach (var num in nums) {
            if (seen_numbers.Contains(num)) {
                return true;
            }
            seen_numbers.Add(num);
        }

        return false;
    }
}