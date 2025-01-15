//https://leetcode.com/problems/parsing-a-boolean-expression/

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:

    char evaluate(vector<char> lst,char op){
        if(op=='&'){
            for(char c:lst){
                if(c=='f')return 'f';
            }
            return 't';
        }
        else if(op=='|'){
            for(char c:lst){
                if(c=='t')return 't';
            }
            return 'f';
        }
        return lst[0]=='t'?'f':'t';
    }
    bool parseBoolExpr(string expression) {
        stack<char> stk;
        int n=expression.size();
        vector<char> lst;
        for(int i=0;i<n;i++){
            char ch=expression[i];
            if(ch==')'){
                lst.clear();
                while(stk.top()!='('){
                    lst.push_back(stk.top());
                    stk.pop();
                }
                stk.pop(); //Remove '('
                char op=stk.top();
                stk.pop();
                char ans=evaluate(lst,op);
                stk.push(ans);
            }
            else{
                if(ch!=','){
                    stk.push(ch);
                }
            }
        }
        return stk.top()=='t';
    }
};

