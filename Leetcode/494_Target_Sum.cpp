//https://leetcode.com/problems/target-sum/
#include <iostream>
#include <vector>
using namespace std;

//This is solution can be optimised by memoization and tabulation
class Solution {
public:
    void recursion(vector<int>& nums,int& target,int index,int cursum,int& count){
        if(index==nums.size()){
            if(cursum==target){
                count++;
            }
            return;
        }
        recursion(nums,target,index+1,cursum+nums[index],count);
        recursion(nums,target,index+1,cursum-nums[index],count);
    }
    int findTargetSumWays(vector<int>& nums, int target) {
        int count=0;
        recursion(nums,target,0,0,count);
        return count;
    }
};