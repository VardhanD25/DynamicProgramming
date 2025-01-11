// https://www.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-increasing-subsequence
#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    // Function to find length of longest increasing subsequence.
    int lis(vector<int>& arr) {
        int n = arr.size();
        vector<int> next1(n + 1, 0); // Stores results for next index
        vector<int> curr(n + 1, 0); // Stores results for current index

        // Loop from the last index to the first
        for (int ind = n - 1; ind >= 0; ind--) {
            for (int prev = ind - 1; prev >= -1; prev--) {
                int nottake = next1[prev + 1]; // Case where current element is not taken
                int take = INT_MIN; // Case where current element is taken

                if (prev == -1 || arr[ind] > arr[prev]) {
                    take = 1 + next1[ind + 1];
                }

                curr[prev + 1] = max(take, nottake);
            }
            next1 = curr; // Update next1 for the next iteration
        }
        
        return next1[0]; // Result is stored in next1[0]
    }
};