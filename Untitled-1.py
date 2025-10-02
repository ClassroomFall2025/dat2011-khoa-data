x = int(input("Nhập bảng cửu chương bạn muốn in: "))
print("Bangcuchuong", x)
for i in range(1, x+1):   
    print("Bangcuchuong", i) 
    for j in range(1,10):     # i là số của bảng (1 → 9)
        print("%d x %d = %d" % (i, j, i * j))
    print()