def maxp(x,y):
    if x >= y:
        return(x)
    else:
        return(y)

print(f'큰 수: {maxp(10,20)}')

a, b = map(int,input().split())
print(f'큰 수: {maxp(a, b)}')