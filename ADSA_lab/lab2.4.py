# merge sort
def merge_sort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(arr,L,R)
        
def merge(arr,L,R):
    i=j=k=0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while i<len(L):
        arr[k]=L[i]
        i+=1
        k+=1
    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1
        
print("Enter the number of elements in the list:")
n=int(input())
arr=[]
for i in range(n):
    print("Enter element",i+1,":")
    arr.append(int(input()))
merge_sort(arr)
print("Sorted array is:",arr)
