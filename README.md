# python-assignment-round2

Impact Analytics Assignment

Question

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. You are not allowed to miss classes for four or more 
consecutive days. Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

The number of ways to attend classes over N days.
The probability that you will miss your graduation ceremony.

Prerequisite
Python 3 must be installed in your local machine.

How to run ?
To run the assignment execute following command:

python main.py

Approach

The brute force way is to generate all possibilites that to attend or not attend class on a particular day. Hence all permutations will be given by (2^n) where
n is the total number of days. Next we have to filter out those permutations where there is absence of 4 or more days to find out the possibilites where I will
miss the graduation ceremony. 

This approach will have exponential time complexity O(2^n) for finding out the total number of possibilities and O(n*2^n) for finding out the possibilites where I will
miss the graduation ceremony, which is very bad.

Optimised approach - 

It can be found out that the given problem is a dynamic programming problem because the problem can be solved by smaller set of problems which occurs again and again
(overlapping subproblems) and if those problems are solved optimally, then the whole problem can be solved optimally (has optimal substructure).

So I have followed bottom up tabulation method to solve this.

At first, I have declared a 2d array dp where dp[i][j] = total no. of ways of attending ith day given that j or more days are consecutively missed, and all the cells
are initialised to 0.

dp[0][0] to dp[0][m-1] (m is defined in the python program) is equal to 1 since for 0 number of total days, there can be only 1 way to attend those 0 classes.

next iterating from 1 to n for i and in the inner loop iterating from m-1 to 0 for j, dp[i][j] will be equal to sum of (total no. of ways of attending 
i-1th day given that 0 or more days are consecutively missed) and (total no. of ways of attending i-1th day given that j+1 or more days are consecutively missed)

hence the relation dp[i][j] = dp[i - 1][0] + dp[i - 1][j + 1]

after that, the corresponding answers can be found out as written in the program.

Now here the space complexity is O(m*n).

Space Optimization - 

But we see that, while filling up the dp table only the previous row of dp is required, hence we can only use one row of dp and a temp array thereby optimising
the space complexity to O(m).
