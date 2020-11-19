def partition(arr,start,end):
    # always take the first element of the subarray as the pivot value
    pivot = arr[start]
    # store the position of the first element of the subarray according to its original position in the array
    i = start
    for j in range(start + 1,end + 1):
        if arr[j] <= pivot:
            # remember how many elements are swapped to the front because they are smaller than the pivot
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    #swap the pivot with the last element that is smaller than the pivot
    arr[start], arr[i] = arr[i], arr[start]
    return i

def quicksort(arr,start,end):
    # if there is only one element in the subarray, bottoms out
    if start >= end:
        return
    else:
        pivot = partition(arr,start,end)
        # the two subarrays left and right to the pivot doesn't have to be sorted
        # by recursively calling quicksort, eventually the left and right subarray will be sorted
        quicksort(arr,start,pivot - 1)
        quicksort(arr,pivot+1,end)
        return True

test_arr = [3,8,5,1,2,4,3,7,10,3]
quicksort(test_arr,0,len(test_arr)-1)
print ("done")



