def longest_common_subsequence(str1, str2):
    rows = len(str1)
    cols = len(str2)

    dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                if dp[i][j - 1] > dp[i - 1][j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

    i = rows
    j = cols
    lcs = ""

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i][j - 1] >= dp[i - 1][j]:
            j -= 1
        else:
            i -= 1

    return lcs, dp[rows][cols]


first_sequence = input("Enter First Sequence: ")
second_sequence = input("Enter Second Sequence: ")

answer, length = longest_common_subsequence(first_sequence, second_sequence)

print("\nLCS is:", answer)
print("Length:", length)