class Solution:

    def uniquePaths(self, A, B):
        # total A-1 downwords steps and B-1 rightwords steps
        # nCr n=A+B-2 r=B-1
        ans = int(math.factorial(A+B-2)/(math.factorial(B-1)*math.factorial(A-1)))
        return ans               
            
