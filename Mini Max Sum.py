# The programs receives a 5 cell array and returns two sums
# one is the minimum sum in the array the other the maximum sum


def miniMaxSum(arr):
    arr = sorted(arr)
    sumMin = sum(arr[:4])
    sumMax = sum(arr[1:])
    print('{} {}'.format(sumMin, sumMax))