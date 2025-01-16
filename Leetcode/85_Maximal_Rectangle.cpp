// https://leetcode.com/problems/maximal-rectangle/

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
int largestRectangleArea(vector<int>& heights) {
        int n=heights.size();
        stack<int> st;
        int ans=0;
        for(int i=0;i<=n;i++){
            while(!st.empty() && (i==n || heights[st.top()]>=heights[i])){
                int height=heights[st.top()];
                st.pop();
                int width;
                if(st.empty())width=i;
                else width=i-st.top()-1;
                ans=max(ans,height*width);
            }
            st.push(i);
        }
        return ans;
    }
    int maximalRectangle(vector<vector<char>>& matrix) {
        int ans=0;
        vector<int> h(matrix[0].size(),0);
        for(int i=0;i<matrix.size();i++){
            for(int j=0;j<matrix[0].size();j++){
                if(matrix[i][j]=='1'){
                    h[j]+=1;
                }
                else h[j]=0;
            }
            ans=max(ans,largestRectangleArea(h));
        }
        return ans;
    }
};

int main(){
    Solution s;
    
    vector<vector<char>> matrix = {
    {'1', '0', '1', '0', '0'},
    {'1', '0', '1', '1', '1'},
    {'1', '1', '1', '1', '1'},
    {'1', '0', '0', '1', '0'}
};

    int a=s.maximalRectangle(matrix);
    cout<<a<<endl;
}