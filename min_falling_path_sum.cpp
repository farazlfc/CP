class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        if(n == 1)
        return *min_element(matrix[0].begin(), matrix[0].end());

        if(m == 1){
            int return_ = 0;
            for(int k =0; k<n; k++){
                return_ += matrix[k][0];
            }
            return return_;
        }

        for(int i = 1;i<n;i++){
            for(int j = 0;j < m; j++){
                if(j == 0)
                matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j+1]);

                if(j== m-1)
                matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j-1]);

                if(j!=0 and j!= m-1)
                matrix[i][j] += min(matrix[i-1][j], min(matrix[i-1][j-1], matrix[i-1][j+1]));
            }
        }
        return *min_element(matrix[n-1].begin(), matrix[n-1].end());
    }
};
