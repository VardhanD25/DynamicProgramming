//https://www.geeksforgeeks.org/problems/longest-common-substring1452/1
#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    int longestCommonSubstr(string& s1, string& s2) {
        // your code here
        int m=s1.size();
        int n=s2.size();
        vector<vector<int>> dp((m+1),vector<int>(n+1,0));
        
        int ans=0;
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                if(s1[i-1]==s2[j-1]){
                    int val=1+dp[i-1][j-1];
                    dp[i][j]=val;
                    ans=max(ans,val);
                }
                else{
                    dp[i][j]=0;
                }
            }
        }
        return ans;

        
    }
};