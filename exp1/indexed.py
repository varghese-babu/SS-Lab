f = [0]*50
index = [0]*50
count = 0
def two():
        count = 0
        for i in range(n):
            print("Enter the next index")
            index[i] = int(input())
            if(f[index[i]]==0):
                count+=1
        if(count==n):
            for i in range(n):
                f[index[i]]=1
            print("Allocated\nFile Indexed\n")
            for k in range(n):
                print(ind,"---->",index[k],":",f[index[k]])
        else:
            print("File in index is already allocated")
            print("Enter another file indexed")
            two()
while(1):
    ind = int(input("Enter the index block"))
    if(f[ind]==0):
        n = int(input("Enter the number of blocks needed"))
        two()
    else:
        print("Index block is allocated")
    print("Do you want to enter more file(Yes - 1/No - 0)")
    c = int(input())
    if(c==0):
        exit()
