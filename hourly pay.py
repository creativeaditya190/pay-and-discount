h=int(input("Enter no of hours: "))

if h>0 and h<=8:
    p=h*100
    
elif h>=9 and h<=12:
    p=800+(h-8)*30
    
elif h>=13 and h<=16:
    p=800+120+(h-12)*40
    
elif h>=17 and h<=20:
    p=800+120+160+(h-16)*50
    
else:
    p=800+120+160+200+(h-20)*60
    
    print("Total wages: ",p)