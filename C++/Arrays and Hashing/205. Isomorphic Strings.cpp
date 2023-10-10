#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size()!=t.size()){
            return false;
        }
        unordered_map<char,char> st;
        unordered_map <char,char> ts;

        for (int i=0; i<s.size(); i++){
            char c1=s[i];
            char c2=t[i];
        
        
        //checking the mapping in both directions
        if(st.find(c1)==st.end()){
            st[c1]=c2;
        }
        else if(st[c1]!=c2){
            return false;
        }

        if(ts.find(c2)==ts.end()){
            ts[c2]=c1;
        }
        else if(ts[c2]!=c1){
            return false;
        }
    }
      return true;
    }
};

//time complexity -> O(n)
//space complexity ->O(n)