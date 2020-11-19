def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(i + 1,len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

test_arr = [7,3,2,4,8,10,12,8,2]
bubblesort(test_arr)
print ("done")