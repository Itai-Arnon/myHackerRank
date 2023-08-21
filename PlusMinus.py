def plusMinus(arr):
    l = [0] * 3
    for i in range(len(arr)):
         if arr[i] > 0:
            l[0] = l[0] +1
         elif arr[i] < 0:
            l[1] = l[1] + 1
         else:
            l[2] = l[2] + 1
    str = '{:.6f}'
    for i in range(len(l)):
        print(str.format(l[i]/len(arr)))

arr = [1,3,4,54,-1,7]
plusMinus(arr)