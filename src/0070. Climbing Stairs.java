class Solution {

    private Map<Integer, Integer> memoizeMap = new HashMap<>();

    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        } else if (memoizeMap.containsKey(n)) {
            return memoizeMap.get(n);
        } else {
            int result = climbStairs(n - 1) + climbStairs(n - 2);
            memoizeMap.put(n, result);
            return result;
        }
    }
}
