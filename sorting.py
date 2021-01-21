arr=[3,2]
print(*arr, sep=',')


def selectionSort(arr):
    n=len(arr)
    for i in range(0,n-1):
        minIndex = i
        for j in range(i+1,n):
            if arr[j]< arr[minIndex]:
                minIndex=j

        arr[i] , arr[minIndex] = arr[minIndex], arr[i]


#selectionSort(arr)

def bubbleSort(arr):
    for i in range(len(arr)-1):
        swp=False
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swp=True
        if swp==False: break

def insertionSort(arr):
    for i in range(1, len(arr)):
            key=i
            while key>0:
                if arr[key] < arr[key-1]:
                    arr[key], arr[key-1] = arr[key-1], arr[key]
                    key-=1
                else: break
def partition(arr,l,r):
    pivot =arr[r]
    pIndex=l
    for i in range(l,r):
        if arr[i]< pivot:
            arr[i],arr[pIndex] = arr[pIndex],arr[i]
            pIndex+=1
    arr[r],arr[pIndex] = arr[pIndex], arr[r]
    return pIndex

def quickSort(arr,l,r):
    if l<r:
        pi = partition(arr,l,r)
        quickSort(arr,l,pi-1)
        quickSort(arr,pi+1,r)


def mergeSort(arr,l,r):
    if l<r :
        m=(r-l)//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)


def countingSort(arr,low,high):


quickSort(arr,0,len(arr)-1)
print(*arr, sep=',')
