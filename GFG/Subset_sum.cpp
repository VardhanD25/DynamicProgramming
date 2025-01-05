//https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
  
    bool func(vector<int>& arr,int index, int target,vector<vector<int>>& dp){
        if(target==0)return true;
        if(index==0)return (arr[0]==target);
        if(dp[index][target]!=-1)return dp[index][target];
        
        bool nottake=func(arr,index-1,target,dp);
        bool take=false;
        if(arr[index]<=target){
            take=func(arr,index-1,target-arr[index],dp);
        }
        return dp[index][target]=take | nottake;
    }

    bool isSubsetSum(vector<int>& arr, int target) {
        // code here
        int n=arr.size();
        vector<vector<int>> dp(n,vector<int>(target+1,-1));
        return func(arr,n-1,target,dp);
        
        
    }

};

//Tabulation Solution 

// class Solution {
//   public:
  

//     bool isSubsetSum(vector<int>& arr, int target) {
//         // code here
//         int n=arr.size();
//         vector<vector<bool>> dp(n,vector<bool>(target+1,false));
        
//         //if target is 0, return true for any index
//         for(int i=0;i<n;i++)dp[i][0]=true;
//         //for index 0, if element at index 0 is equal to target return true
//         dp[0][arr[0]]=true;
        
//         for(int index=1;index<n;index++){
//             for(int t=1;t<=target;t++){
//                 bool nottake=dp[index-1][t];
//                 bool take=false;
//                 if(arr[index]<=t){
//                     take=dp[index-1][t-arr[index]];
//                 }
//                 dp[index][t]=take|nottake;
//             }
//         }
//         return dp[n-1][target];
        
        
//     }

// };