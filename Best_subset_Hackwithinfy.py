from itertools import permutations
N = int(input())
A = []
for i in range(0,N,1):
    A.append(int(input()))
arr= []   
for i in range(0,N):   
    for j in range(i,N):  
        arr.append(A[i:(j+1)])
        
def check_triangle(Z):
    count = 0
    B=[]
    B=list(permutations(Z,3))
    for i in B:
        a=i[0]
        b=i[1]
        c=i[2]
        if(a+b>c and a+c>b and b+c>a):
            count = count+1
    if (count==len(B)):
        return len(Z)
    else:
        return -1
size1=0
arr1=[]
for i in arr:
    if len(i)<3:
        continue
    else:
        size1 = check_triangle(i)
        arr1.append(size1)
arr1.sort()
print(arr1[len(arr1)-1])
        
