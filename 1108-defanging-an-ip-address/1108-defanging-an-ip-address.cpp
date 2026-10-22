class Solution {
public:
    string defangIPaddr(string address) {
        string na;
        for(int i = 0; i < address.length(); i++){
            if(address[i] == '.'){
                na =na + "[.]";
            }
            else{
                na=na+address[i];
            }
        }
        return na;
    }
};