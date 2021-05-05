a = input("ENTER CHAR WITH ONLY A&B :\n")
current = 0
next1 = 1
sum1 = 0
print(len(a))
while(next1<len(a)):
    if(a[current] ==a[next1]):
        sum1 =  sum1 +1
        current = current + 1
        next1 = next1 + 1
    else:
        current = current +1
        next1 = next1 + 1
if (sum1>0):
    print("you need to remove",sum1," char")
else:
    print("you dont need to remove any")
