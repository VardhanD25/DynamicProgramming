// https://www.geeksforgeeks.org/problems/geek-jump/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=geek-jump
//Similar to the climbing stairs problem (Leetcode 70)
#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    int minimumEnergy(vector<int>& height, int n) {
        
        int spent=0;
        int index=0;
        vector<int> energy(n,-1);
        if(n==1){
            return 0;
        }
        energy[0]=0;
        energy[1]=abs(height[0]-height[1]);
        for(int i=2;i<n;i++){
            energy[i] = min(
                energy[i-1] + abs(height[i] - height[i-1]),
                energy[i-2] + abs(height[i] - height[i-2])
            );

        }
        return energy[n-1];
    }
};

