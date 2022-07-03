#Program 3:

def pascals_triangle(n):
    list1=[]
    for i in range(n):
        list2=[]
        for j in range(i+1):
            if j==0 or j==i:
                list2.append(1)
            else:
                list2.append(list1[i-1][j-1]+list1[i-1][j])
        list1.append(list2)

    for i in range(n):
        for j in range(n-i-1):
            print(format("","<2"),end="")
        for j in range(i+1):
            print(format(list1[i][j],"<4"),end="")
        print()
num=int(input("Enter number of rows: "))
print(pascals_triangle(num))
