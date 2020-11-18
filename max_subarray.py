def find_max_crossing_subarray(arr,start,mid,end):
    left_sum = -1000000
    sum = 0
    max_left = 0
    for l in range(mid,start - 1,-1):
        # Make sure this is updating the sum using sum, not using left_sum; left_sum is set to just let the first element added to sum as default
        sum = sum + arr[l]
        if sum > left_sum:
            left_sum = sum
            max_left = l

    right_sum = -1000000
    sum = 0
    max_right = 0
    # mid + 1: Make sure the loop starts at the index next to the midpoint (i.e. the first element in the right subarray)
    for r in range(mid + 1,end + 1):
        sum = sum + arr[r]
        if sum > right_sum:
            right_sum = sum
            max_right = r
    print (left_sum, right_sum)
    return (max_left,max_right,left_sum + right_sum)


"""
Divide: divide the array into subarrays
Conquer: find the maximum subarray in either: 1) within the left subarray; 2) within the right subarray; 3) between left and right subarray
Combine: compare the maximum subarray of left, right and between and see which one has the maximum value
"""
def find_max_subarray(arr,start,end):
    # Conquer: when only one element is in the node, just return that element as the maximum subarray
    if start == end:
        return (start,end,arr[end])
    else:
        # int(mid): make sure to make mid an int to prevent infinite loop (because float can divide by 2 indefinitely before reaching 0)
        mid = int((start + end) / 2)
        (left_start, left_end, left_sum) = find_max_subarray(arr,start,mid)
        (right_start, right_end, right_sum) = find_max_subarray(arr,mid+1,end)
        (max_left, max_right, cross_sum) = find_max_crossing_subarray(arr,start,mid,end)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_start, left_end, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_start, right_end, right_sum)
        else:
            return (max_left, max_right, cross_sum)

def main():
    test_arr = [0,13,-3,-25,-20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    (buy, sell, profit) = find_max_subarray(test_arr,0,len(test_arr)-1)
    print ("Buy at day {}; Sell at day {}; Profit at {}".format(buy,sell,profit))
    return True

main()
