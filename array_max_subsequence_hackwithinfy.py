N = int(input())
A =[]
for i in range(0,N,1):
    A.append(int(input()))
SubA=[]
lenofsubA=[]
for i in range(0,N,1):
    first = A[i]
    list1 =[first]
    for j in range(i+1,N,1):
        if first<=A[j]:
            list1.append(A[j])
            first = A[j]
    SubA.append(list1)
    lenofsubA.append(len(list1))
    
max_value = max(lenofsubA)                    
max_index=lenofsubA.index(max_value)

total = sum(SubA[max_index])
print(total)

                     

