def merge(left, right):
    result = []
    i,j = 0, 0
    while i<len(left) and j<len(right):
        if(left[i] <= right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(lst):
    if(len(lst) <= 1):
        return lst
    mid = int(len(lst)/2)
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left, right)

arr = [1,4,5,6,7,2,45,76,23,10,11,12,13,99,150,154,15,16]
print(mergesort(arr))
