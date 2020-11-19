def merge(arr,start,mid,end):
    nl = mid - start + 1
    nr = end - mid
    left = []
    right = []
    for l in range(nl):
        left.append(arr[start+l])
    for r in range(nr):
        right.append(arr[mid+1+r])

    # add sentinel element so that, if one subarray runs out of elements to compare, there is still this sentinel element that the other subarray can compare with (and always smaller than the sentinel), and can put all the remaining elements back to the array
    left.append(1000000)
    right.append(1000000)

    i = 0
    j = 0
    # for loop counts from the starting index to the ending index, making sure all elements of the array are compared, and are placed at the correct order
    for k in range(start,end+1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
    return arr

def mergesort(arr,start,end):
    if start < end:
        mid = int((start + end) / 2)
        #depth-first traversal to the end of the left most node
        mergesort(arr,start,mid)
        # at each level, traverse to the right node
        mergesort(arr,mid + 1,end)
        #merge the two nodes at the level
        merge(arr,start,mid,end)
        # traverse back to the parent node
    # if the node has only 1 element, then traverse back to the parent node

def main():
    test_arr = [7,4,6,3,10,2,9,8,10,12]
    mergesort(test_arr,0,len(test_arr)-1)
    return True

main()