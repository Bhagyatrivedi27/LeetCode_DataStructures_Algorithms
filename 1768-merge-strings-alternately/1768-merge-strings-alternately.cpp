class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        string output = "";
        
        int i1=0, i2=0;
        bool flag = false;
        
        while(i1<n or i2<m){
            if(flag and i2<m){
                output += word2[i2++];
            }else if(!flag and i1<n){
                output += word1[i1++];
            }
            flag = !flag;
        }    
        
        return output;
    }
};