// https://www.geeksforgeeks.org/problems/geeks-training/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=geeks-training
#include<iostream>
#include <vector>
using namespace std;

class Solution {
  public:
  
    int recur(int day,int last,vector<vector<int>>& arr, vector<vector<int>>& dp){
        if(dp[day][last]!=-1)return dp[day][last];
        
        if(day==0){
            int maxi=INT_MIN;
            for(int task=0;task<=2;task++){
                if(task!=last){
                maxi=max(maxi,arr[0][task]);
                }
            }
            return dp[day][last]=maxi;
        }
        int maxi=INT_MIN;
        for(int task=0;task<=2;task++){
            if(task!=last){
                int points=arr[day][task]+recur(day-1,task,arr,dp);
                maxi=max(maxi,points);
            }
        }
        return dp[day][last]=maxi;
    }
    int maximumPoints(vector<vector<int>>& arr, int n) {
        // Code here
        vector<vector<int>> dp(n,vector<int>(4,-1));
        return recur(n-1,3,arr,dp);
    }
};