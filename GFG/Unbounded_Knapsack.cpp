// /https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=knapsack-with-duplicate-items

#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    int knapSack(vector<int>& val, vector<int>& wt, int capacity) {
        // code here
        int n=wt.size();
        vector<vector<int>> dp(n,vector<int>(capacity+1,0));
        
        for(int cap=1;cap<=capacity;cap++){
            if(cap>=wt[0]){
                dp[0][cap]=val[0]*(cap/wt[0]);
            }
        }
        for(int i=1;i<n;i++){
            for(int cap=0;cap<=capacity;cap++){
                int nottake=dp[i-1][cap];
                int take=INT_MIN;
                if(wt[i]<=cap){
                    take=val[i]+dp[i][cap-wt[i]];
                }
                dp[i][cap]=max(take,nottake);
            }
        }
        return dp[n-1][capacity];
        
    }
};