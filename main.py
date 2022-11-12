# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solve(n,m):
    """
            Time Complexity: O(m * n)
            Space Complexity: O(m)
            Dynamic Programing Tabulation with Space Optimization
            """
    dp = [1] * (m + 1)
    dp[m] = 0

    for i in range(1, n + 1):
        temp = [0] * (m + 1)    #dp[i][j] represents total no. of ways of attending ith day given that j or more days are consecutively missed
        for j in range(m - 1, -1, -1):
            temp[j] = dp[0] + dp[j + 1]
        temp, dp = dp, temp

    x1 = dp[0]  # total number of valid way to attend classes
    x2 = temp[1]  # total number of way to miss last day

    print("The number of ways in which to attend classes and not miss the graduation ceremony: " + str(x1-x2))
    print("The probability that graduation ceremony will be missed: " + f"{x2}/{x1}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input('Enter total number of days(n) where the last day is the graduation day: '))
    m = int(input('Enter number of days < n greater than or equal to which cannot be missed consecutively otherwise graduation ceremony'
                  ' cannot be attended(m): '))
    solve(n,m)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
