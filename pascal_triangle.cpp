class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        vector<int> x(1,1);
        ans.push_back(x);
        if(numRows == 1)
        return ans;

        vector<int> y(2,1);
        ans.push_back(y);

        if(numRows == 2)
        return ans;

        for(int i = 3; i<= numRows; i++){
            vector<int> temp;
            temp.push_back(1);
            for(int j = 0; j <i-2;j++){
                int curr = ans[i-2][j] + ans[i-2][j+1];
                temp.push_back(curr);}
            temp.push_back(1);
            ans.push_back(temp);

        }
        return ans;

        
    }
};
