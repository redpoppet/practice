from type import List 

class Insertion(Object):
    def sort(lst: List[int]):
        n  =  len(lst)
        for i in range(1,n):
            for j in range(i,1,-1):
                if lst[j-1]>lst[i]:
                    exch(i,j)
                