
def getMoneySpent(keyboards, drives, b):
    n1 = len(keyboards)
    n2 = len(drives)
    keyboards.sort()
    drives.sort()
    i=0
    j=n2-1
    result = -1
    while i < n1 and j >=0:
        price = keyboards[i]+drives[j]
        if price == b: return price
        elif price > b: j-=1
        else:
            i+=1
            if price > result: result = price

    return result
if __name__ == '__main__':

    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)
