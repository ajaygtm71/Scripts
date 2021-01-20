def findPosition(arr, l, r, x):
    if l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            if mid>l and x>arr[mid-1]: return mid
            else: return findPosition(arr, l, mid - 1, x)
        else:
            if mid<r and x<arr[mid+1]: return mid+1
            else: return findPosition(arr, mid + 1, r, x)
    return -1


class Solution:
    def printKClosest(self, arr, n, k, x):
        if x<arr[0]: return arr[0:k]
        elif x>arr[n-1]: return reversed(arr[n-k:])

        idx = findPosition(arr, 0, n - 1, x)
        #print(idx)
        i=idx-1
        j=idx
        if arr[idx]==x: j+=1
        temp=list()
        while i>=0 and j<n and k>0:
            if x-arr[i] < arr[j]-x:
                temp.append(arr[i])
                i-=1
            else:
                temp.append(arr[j])
                j+=1
            k-=1
        while i<0 and k>0:
            temp.append(arr[j])
            j+=1
            k-=1
        while j>n-1 and k>0:
            temp.append(arr[i])
            i-=1
            k-=1
        return (temp)

if __name__ == '__main__':

    arr = [36 ,146, 154, 170 ,282 ,293, 300, 323 ,335, 359 ,383 ,392, 422 ,437, 448 ,465, 468 ,479, 492 ,501,
           539, 605 ,668 ,704 ,706 ,717, 719 ,725 ,727 ,772 ,812 ,828, 828 ,870 ,895 ,896, 903 ,913 ,943, 962, 963 ,996]
    n = len(arr)
    k, x = 8, 996
    ob = Solution()
    ans = ob.printKClosest(arr, n, k, x)
    for xx in ans:
        print(xx, end=" ")
    print()
