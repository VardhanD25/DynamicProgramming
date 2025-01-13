// https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=matrix-chain-multiplication

#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    int matrixMultiplication(vector<int> &arr) {
        // code here
        int n=arr.size();
        vector<vector<int>> dp(n,vector<int>(n,-1));
        return recur(arr,1,n-1,dp);
        
        
    }
    
    int recur(vector<int>& arr,int i,int j,vector<vector<int>>& dp){
        if(i==j)return 0;
        if(dp[i][j]!=-1)return dp[i][j];
        int mini=INT_MAX;
        for(int k=i;k<j;k++){
            mini=min(mini,arr[i-1]*arr[k]*arr[j]+recur(arr,i,k,dp)+recur(arr,k+1,j,dp));
        }
        return dp[i][j]=mini;
    }
};

//Tabulation solution

// class Solution {
//   public:
//     int matrixMultiplication(vector<int> &arr) {
//         // code here
//         int n=arr.size();
//         vector<vector<int>> dp(n,vector<int>(n,0));
        
//         for(int i=n-1;i>=1;i--){
//             for(int j=i+1;j<n;j++){
//                 int mini=INT_MAX;
//                 for(int k=i;k<j;k++){
//                     mini=min(mini,arr[i-1]*arr[k]*arr[j]+dp[i][k]+dp[k+1][j]);
//                 }
//                 dp[i][j]=mini;
//             }
//         }
//         return dp[1][n-1];
        
        
//     }
    
// };