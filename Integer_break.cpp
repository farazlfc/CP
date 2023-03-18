class Solution {
public:
    int integerBreak(int n) {
        if (n==2)
        return 1;

        if(n==3)
        return 2;

        int rem;
        int fac;
        rem = n%3;
        fac = n/3;
         if(rem == 1)
             return pow(3, fac - 1)*4;
         if(rem == 0)
             return pow(3, fac);
        return pow(3, fac)*2;
    }
};
