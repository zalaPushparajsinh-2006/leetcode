class Solution {
public:
    int mostFrequentEven(vector<int>& nums) {
        unordered_map<int,int> x;
        int n=nums.size(),mx=0,z=-1;
        for(int i=0;i<n;i++){
            if(nums[i]%2==0){
                x[nums[i]]++;
                if(x[nums[i]]>mx){
                    z=nums[i];
                    mx=x[nums[i]];
                }
                else if(x[nums[i]]==mx && nums[i]<z){
                    z=nums[i];
                }
            }
        }
        return z;
    }
};