def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    print("Sorted array is:",arr)
    
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
    print("Sorted array is:",arr)


def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
        
    print("Sorted array is:",arr)           

def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
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

def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[l]>arr[largest]:
        largest=l
    if r<n and arr[r]>arr[largest]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def heap_sort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    print("Sorted array is:",arr)
    
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        less=[x for x in arr[1:] if x<=pivot]
        greater=[x for x in arr[1:] if x>pivot]
        return quick_sort(less)+[pivot]+quick_sort(greater)
    
    
    
arr=[]
print("Enter the number of elements in the list:")
n=int(input())
for i in range(n):
    print("Enter element",i+1,":")
    arr.append(int(input()))

bubble_sort(arr)
insertion_sort(arr)
selection_sort(arr)
merge_sort(arr)
print("Sorted array is:",arr)
heap_sort(arr)
q=quick_sort(arr)
