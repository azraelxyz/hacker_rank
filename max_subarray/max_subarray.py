'''
Given an array  of  elements, find the maximum possible sum of a

Contiguous subarray
Non-contiguous (not necessarily contiguous) subarray.
Empty subarrays/subsequences should not be considered.

https://www.hackerrank.com/challenges/maxsubarray?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=3-day-campaign

'''

import sys

T = int(sys.stdin.readline())


def max_contiguous_subarray(arr, N):
    max_sum = -sys.maxint - 1
    max_ending_here = 0

    for i in range(N):
        max_ending_here = max_ending_here + arr[i]
        if max_sum < max_ending_here:
            max_sum = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_sum


def max_non_contiguous_subarray(arr):
    arr.sort()
    subarray = []
    for x in arr:
        if x > 0:
            subarray.append(x)

    if len(subarray) > 0:
        return sum(subarray)
    else:
        return max(arr)

for _ in range(T):
    N = int(sys.stdin.readline())
    mylist = [int(x) for x in sys.stdin.readline().strip().split(' ', N-1)]

    print max_contiguous_subarray(mylist, N), max_non_contiguous_subarray(mylist)
