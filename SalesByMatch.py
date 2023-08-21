# 1 month preparation kit  Week 2  SalesBy Match
# Given Array of colored socks each int represents a color
# Find number of pair of the same colors
# count only pairs
import random

max_length = 100
max_no_colors = 100
n = 100
colored_socks = []
for x in range(n):
    colored_socks.append(random.randrange(1, n))

col1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]

for x in range(len(col1), n):
    col1.append(0)

print(col1)


# [10, 20, 20, 10, 10, 30, 50, 10, 20]


# [3,3,5,5,6,6,7


def sockMerchant(n, ar):
    socks_by_color = [0] * 100
    no_of_pairs = 0
    for i in range(0, len(ar)):
        if ar[i] != 0:
            socks_by_color[ar[i]] += 1

    for i in range(0, n):
        no_of_pairs += (socks_by_color[i] // 2)
    return no_of_pairs

col2 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
col3 = [1,2,1,2,1,3,2]
print(sockMerchant(n, col3))
