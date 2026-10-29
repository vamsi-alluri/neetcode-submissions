public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> numsSet = new();
        for (int i = 0; i < nums.Length; i++){
            if (!numsSet.Add(nums[i])){
                return true;
            }
        }
        return false;
    }
}