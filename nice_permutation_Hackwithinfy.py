N = int(input())
int_arr = []
count = 0
for i in range(1,N+1,1):
    int_arr.append(i)

def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l


def check(list2,t):
    b = 0
    c = t
    for k in range(len(list2)):
        if k==0:
            x=list2[k]%2
            y=list2[k+1]%2
            if x==y:
                b = b+1
        elif k==len(list2)-1:
            x=list2[k]%2
            z=list2[k-1]%2
            if x==z:
                b=b+1
        else:
            x=list2[k]%2
            y=list2[k+1]%2
            z=list2[k-1]%2
            if x==y or x==z:
                b = b+1
    if b == c:
        return 1
    
for p in permutation(int_arr):
    a =check(p,N)
    if a == 1:
       count = count +1

print(count)
