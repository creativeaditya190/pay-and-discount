p1=float(input("Enter price of prodct 1 : "))
p2=float(input("Enter price of prodct 2 : "))
p3=float(input("Enter price of prodct 3 : ")) 

t=p1+p2+p3

if t>0 and t<=9:
    d=0
    
elif t>=10 and t<=99:
    d=5/100*t
    
elif t>=100 and t<=499:
    d=10/100*t
    
elif t>=500 and t<=999:
    d=15/100*t
    
else:
    d=20/100*t
    
    f=t-d
    
    print("Total price: Rs ",round(t,2))
    print("Discount price: Rs ",round(d,2))
    print("Finakl payment: Rs ",round(f,2))