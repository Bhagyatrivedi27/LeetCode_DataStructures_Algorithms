class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        
        int n = arr.size();
        vector<int>incT(n+1);
        vector<int>decT(n+1);
        int res=1;
        incT[0] = decT[0] = 1;
        
        for(int i=0;i<n;i++){
            if(i==0)
                continue;
            if(arr[i] < arr[i-1]){
                decT[i] = 1 + incT[i-1];
                incT[i] = 1;
            }
            if(arr[i]>arr[i-1]){
                incT[i] = 1+decT[i-1];
                decT[i]=1;
            }
            if(arr[i] == arr[i-1]){
                incT[i] = decT[i] = 1;
            }
            res = max(res, max(incT[i], decT[i]));
        }
        return res;
    }
};