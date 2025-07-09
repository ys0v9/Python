#45-0
print('< 45-0>')
a = int(input("행 수: "))
for i in range(a):  
    for j in range(a): 
        print('*', end='')
    print()  
print()

#45-1
print('< 45-1 >')
b=int(input("행 수: "))
for i in range(1,b+1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

#45-2
print('< 45-2 >')
c=int(input("행 수: "))
for i in range(c,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

#45-3
print('< 45-3 >')
d=int(input("행 수: "))
for i in range(1, d+1):
    for j in range(d-i):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()
print()

#45-4
print('< 45-4 >')
e=int(input("행 수: "))
for i in range(e,0,-1):
    print(" "* (e-i)+"*" * i )
print()

# #45-5
# f = int(input('행 수: '))
# for i in range(1,f+1):
#     for j in range(f-i):