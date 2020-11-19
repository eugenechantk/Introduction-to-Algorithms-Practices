"""
Building a max heap: making sure that A[Parent(i)] >= A[i] at every i
"""
def build_max_heap(arr):
    # only need to traverse half of the node in the heap; only half of the nodes have children nodes
    for i in range(int(len(arr)/2),-1,-1):
        max_heapify(arr,i,len(arr)-1)
    return arr

"""
Max Heapify: making sure that the node at A[i] >= A[Left(i)] and A[Right(i)], Left(i) and Right(i) being A[i]'s two children node
Complexity: O(log n), because it only traverse through offsprings of the starting index, at max it will only traverse for the height of the heap (i.e lg n)
"""
def max_heapify(arr,i,heap_size):
    l = i * 2 + 1
    r = i * 2 + 2
    # l <= heap_size; making sure that if there is no left child node, don't compare and swap
    if l <= heap_size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    
    # r <= heap_size; make sure that if there is no right child node, don't compare and swap
    if r <= heap_size and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        # only swap places with the largest value node when finish comparing both left and right child
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr,largest,heap_size)

    return True

def heapsort(arr):
    heapsize = len(arr)-1
    arr = build_max_heap(arr)
    for i in range(len(arr)-1):
        arr[0], arr[heapsize - i] = arr[heapsize - i], arr[0]
        # removing the last element out of the heap by reducing the heapsize by 1
        max_heapify(arr,0,heapsize - i - 1)

def main():
    test_arr = [4,1,3,2,16,9,10,14,8,7]
    heapsort(test_arr)
    return True

main()