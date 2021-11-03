def coomon_subsequence_count(s,t):
    n1=len(s)
    n2=len(t)
    dp=[[0 for i in range( n2+1)]
         for j in range(n1+1)]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=1+dp[i][j-1]+dp[i-1][j]
            else:
                dp[i][j]=dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]
    return dp[n1][n2]
s=str(input("Enter rhe input string"))  
t=str(input("Enter rhe input string"))  
print(coomon_subsequence_count(s,t))              

