class Solution {
public:
    string frequencySort(string s) {
        int n = s.length();

        vector<int> mp(128,0);

        for(char c : s) mp[c]++;

        string t = s;
        sort(t.begin(), t.end(), [&](char a, char b){
            return mp[a] > mp[b] ||(mp[a] == mp[b] && a < b);
        });

        return t;

    }
};