def find_max_crossing_subarray(arr,start,mid,end):
    left_sum = -1000000
    sum = 0
    max_left = 0
    for l in range(mid,start - 1):
        sum = left_sum + arr[l]
        if sum > left_sum:
            left_sum = sum
            max_left = l
    
    right_sum = -1000000
    sum = 0
    max_right = 0
    for r in range(mid,end + 1):
        sum = right_sum + arr[r]
        if sum > right_sum:
            right_sum = sum
            max_right = r
    
    return (max_left,max_right,left_sum + right_sum)

