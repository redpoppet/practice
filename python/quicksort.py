
def quickSort(lst):
    left =  0
    right = len(lst) -1 
    if left>=right:
        return 
    key = lst[left]
    while(left<right):
        while(left<right and lst[right]>key):
            right = right -1 
        if left<right:
            lst[left]=lst[right]
            left = left + 1
        while(left<right and lst[left]<key):
            left = left + 1
        if left <right:
            lst[right] = lst[left]
            right = right -1 
    
    lst[left] = key 
    # print(left)
    quickSort(lst[left+1:])
    quickSort(lst[:left-1])
    # quickSort(lst,left+1,end)
    # quickSort(lst,start,left-1)
    return lst 

a = [1,3,2,8,3,0,4,5,2]

print(quickSort(a))


