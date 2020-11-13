class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        # FIND THE POSTIONS OF THE INVALID OPEN AND CLOSED BRACKETS
        opens = []
        closes = []
        
        # LOOP THROUGH THE STRING
        for i in range(len(s)):
            
            # AN OPEN BRACKET - IT COULD BE VALID OR NOT, BUT WE'RE GUARANTEED THAT ALL LEFTOVER BRACKETS IN OPENS WILL BE INVALID AFTER EXITING THE LOOP
            if s[i] == '(':
                opens.append(i)
                
            # A VALID CLOSED BRACKET
            elif opens:
                opens.pop()
                
            # AN INVALID CLOSED BRACKET
            else:
                closes.append(i)
         
        # EDGE CASE : NO INVALID BRACKETS
        if not opens and not closes:
            return len(s)
        
        # GATHER A SINGLE ARRAY OF OPENED AND CLOSED BRACKET (WRITE A O(N) MERGE HERE)
        n1,n2 = len(opens),len(closes)
        if n1 == 0:
            merged = closes
        elif n2 == 0:
            merged = opens
        else:
            merged = []
            i,j = 0,0
            while i<n1 and j<n2:
                if opens[i]  < closes[j]:
                    merged.append(opens[i])
                    i+=1
                else:
                    merged.append(closes[j])
                    j+=1
            while  i<n1:
                merged.append(opens[i])
                i+=1
            while j < n2:
                merged.append(closes[j])
                j+=1
            
                    
        #merged = sorted(opens + closes)
        
        # GET THE MAXIMUM DIFF
        return self.max_diff(merged, len(s))
    
    def max_diff(self, merged, n):
        merged =[-1] + merged + [n]
        diff = 0
        for i in range(1, len(merged)):
            diff = max(diff, merged[i] - merged[i - 1] - 1)
        return diff
