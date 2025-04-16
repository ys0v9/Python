# #44-1
# row=int(input("행: "))
# column=int(input("열: "))

# for i in range(1,row+1):
#     for j in range(1, column+1): 
#         print(i*j, end=" ")
#     print()


#44-2
h = int(input("행: "))
y = int(input("열: "))
for i in range(1, h * y + 1):
    print(i, end=" ")
    if i % y == 0:
        print()