//https://www.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1
#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    int LongestBitonicSequence(int n, vector<int> &arr) {
        // code here
        vector<int> fwd(n,1),bwd(n,1);
        //Longest Increasing Subsequence
        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                if(arr[i]>arr[j] && fwd[j]+1>fwd[i]){
                    fwd[i]=1+fwd[j];
                }
            }
        }
        // Longest Decreasing Subsequence
        for(int i=n-2;i>=0;i--){
            for(int j=n-1;j>i;j--){
                if(arr[i]>arr[j] && bwd[j]+1>bwd[i]){
                    bwd[i]=bwd[j]+1;
                }
            }
        }
        int maxi=INT_MIN;
        //Calculating longest bitonic by merging increasing and decreasing
        for(int i=0;i<n;i++){
            if(fwd[i]==1 || bwd[i]==1)continue; //to ensure that both inc and dec parts are not empty
            maxi=max(maxi,fwd[i]+bwd[i]-1); // -1 to ensure same element is not counted twice
        }
        if(maxi==INT_MIN)return 0;
        return maxi;
    }
};