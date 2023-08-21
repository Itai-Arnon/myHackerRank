
'''  given is a list of integers, , and a single integer . You must create an array of length k
from elements of  such hat its unfairness is minimized. Call that array . Unfairness of
an array is calculated
  a_tag is a k length array. Find the a_tag array where   max_array_member - min_array_member is minimum
  i.e the unfairness is minimized
'''
import random
def build_arr(length):
    _arr = []
    for i in range(length):
        _arr.append(int( round((random.random()) * 10, 0)))
    return _arr


# arr = [1,3,4,5]
k = 2   #  int(random.randrange(2,5))
arr = build_arr(3)
arr = sorted(arr)

min_unfairness = arr[k] - arr[0]
length = len(arr) - k
for x in range(length):
    # sliding window type question
    if min_unfairness > (arr[x+k] - arr[x]):
        min_unfairness = (arr[x+k] - arr[x])
print('K: {}'.format(k))
print("The Array:")
print( *arr)
print ('Min Unfairness: {}'.format(min_unfairness))