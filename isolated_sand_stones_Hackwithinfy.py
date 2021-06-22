from itertools import product
N =int(input())
M =int(input())
X =int(input())
wos=list(range(1,M+1))
arr=[]
count =0 
def check_possible(list1,a,b):
    count1 = 0
    if sum(list1)==a:
        for i in list1:
            if i>=b:
                count1+=1
    if(count1>0):
        return 1
    else:
        return 0
    
for r in range(1,N+1):
    for c in product(wos,repeat=r):
        a = check_possible(c,N,X)
        if a==1:
            count +=1
print(count)
        
    

