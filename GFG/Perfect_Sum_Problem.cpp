//https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=perfect-sum-problem

#include <iostream>
#include <vector>
using namespace std;
class Solution {
  public:
    int perfectSum(vector<int>& arr, int target) {
        int n = arr.size();
        vector<vector<int>> dp(n, vector<int>(target + 1, 0));

        // Base case: forming a sum of 0 is always possible by taking no elements
        for (int i = 0; i < n; i++) {
            dp[i][0] = 1;
        }

        // Base case for the first element
        if (arr[0] <= target) dp[0][arr[0]] = 1;
        if(arr[0]==0)dp[0][0]=2; //If first element is zero, whether it is included or not included,
        //the target remains same, but 2 combinations have to be counted

        for (int index = 1; index < n; index++) {
            for (int tar = 0; tar <= target; tar++) {
                int take = 0;
                if (arr[index] <= tar) {
                    take = dp[index - 1][tar - arr[index]];
                }
                int notTake = dp[index - 1][tar];
                dp[index][tar] = take + notTake;
            }
        }

        return dp[n - 1][target];
    }
};