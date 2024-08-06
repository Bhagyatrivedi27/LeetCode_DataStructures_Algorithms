class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int n= arr.size();
        vector<int> incT(n);
        vector<int> decT(n);
        
        //Smallest problem
        incT[0] = decT[0] = 1;
        int res = 1;
        for(int i=1;i<n;i++){
            if(arr[i] > arr[i-1]){
                incT[i] = 1+decT[i-1];
                decT[i] = 1;
            }
            if(arr[i] < arr[i-1]){
                decT[i] = 1+incT[i-1];
                incT[i] = 1;
            }
            if(arr[i] == arr[i-1]){
                decT[i] = 1;
                incT[i] = 1;
            }
            res = max(res,max(decT[i], incT[i]));
        }
        
        return res;
    }
};