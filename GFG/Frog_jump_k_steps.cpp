#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    int minimizeCost(int k, vector<int>& arr) {
        // Code here
        int spent=0;
        int n=arr.size();
        vector<int> energy(n,-1);
        if(n==1){
            return 0;
        }
        energy[0]=0;
        energy[1]=abs(arr[0]-arr[1]);
        for(int i=2;i<n;i++){
            int mini=INT_MAX;
            for(int j=1;j<=k;j++){
                if(i-j<0)break;
                int val=energy[i-j]+abs(arr[i]-arr[i-j]);
                mini=min(mini,val);
            }
            energy[i]=mini;

        }
        return energy[n-1];
        
    }
    
};