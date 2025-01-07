//https://www.geeksforgeeks.org/problems/rod-cutting0840/1

#include <iostream>
#include <vector>
using namespace std;



class Solution {
  public:
    int cutRod(vector<int> &price) {
        // code here
        int n=price.size();
        vector<vector<int>> dp(n,vector<int>(n+1,0));
        
        for(int remaining=1;remaining<=n;remaining++){
            dp[0][remaining]=price[0]*remaining;
        }
        for(int i=1;i<n;i++){
            for(int rem=0;rem<=n;rem++){
                int nottake=dp[i-1][rem];
                int take=INT_MIN;
                if(i+1<=rem){
                    take=price[i]+dp[i][rem-i-1];
                }
                dp[i][rem]=max(take,nottake);
            }
        }
        return dp[n-1][n];
    }
};

