class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.size();
        
        
        int left=0, right =0, longestValid=0;
        
        for(int i=0;i<n;i++){
          
            if(s[i] == '(')
                left++;
            else
                right++;
            
            if(left==right){
                longestValid = max(longestValid, left * 2);
            }
            
              if(right>left){
                left = 0;
                right = 0;
            }
            
            
        }
        
        left =0, right=0;
        for(int i=n-1;i>=0;i--){
            
            if(s[i] == '(')
                left++;
            if(s[i] == ')')
                right++;
            if(left==right){
                longestValid = max(longestValid, left * 2);
            }
            
             if(right<left){
                left = 0;
                right = 0;
            }
            
        }
        return longestValid; 
    }
};