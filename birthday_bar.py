
def birthday(squares,d,m):
    n =len(squares)
    block = sum(squares[:m])
    count=0
    if block ==d : count+=1
    for i in range(1,n-m+1):
        #print(squares[i:i+m])
        block = block - squares[i-1] + squares[i+m-1]
        if block == d: count += 1
        #print(block)
    return count

if __name__ == '__main__':
    n= int(input())
    squares = list(map(int,input().split()))
    d,m = list(map(int,input().split()))
    print(birthday(squares,d,m))
