i_n = [101,102,103,104]
price=[42,50,500,40]
stock=[10,20,15,16]
a=0
n = int(input())
m = int(input())
for i in range(0,len(i_n),1):
    if(n ==i_n[i]):
        a=1
        if(m<=stock[i]):
            print( m*price[i]/1,"INR")
        else:
            print("NO STOCK")
            m=0
        print(stock[i]-m,"LEFT")
if (a==0):
    print("INVALID INPUT")
