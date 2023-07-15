#You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) 
#so that the sum of contiguous elements is maximum. 
#But the sum must not exceed B.
#Input   A = 5   B = 12    C = [2, 1, 3, 4, 5]
#Output    12

def MaxSubArray(size_of_array,maximum,array):
    maxsum = -float('inf')
    Sum=0
    start=0
    end=0
    while end < size_of_array:
        Sum += array[end]
        while Sum > maximum:
            Sum -= array[start]
            start += 1
        maxsum = max(maxsum, Sum)
        end += 1
    return maxsum

size_of_array=5
maximum=12
array=[2,1,3,4,5]
print(MaxSubArray(size_of_array,maximum,array))