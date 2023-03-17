class Solution {
public:
    int nthUglyNumber(int n) {
        //2, 3 and 5
        vector<int> dp(n+1, 1);
        int i;
        int ptr2 = 1;
        int ptr3 = 1;
        int ptr5 = 1;

        //increment more than one if required basically
        for(i=2;i<=n;i++){
            int val2 = 2*dp[ptr2];
            int val3 = 3*dp[ptr3];
            int val5 = 5*dp[ptr5];

            int min_val = min(min(val2, val3), val5);

            dp[i] = min_val;

            if(min_val == val2)
            ptr2++;

            if(min_val == val3)
            ptr3++;

            if(min_val == val5)
            ptr5++;

        }
        return dp[n];

        
    }
};
