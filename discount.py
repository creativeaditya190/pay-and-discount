#discount calculation project
q=int(input("Enter no of item : "))
if q>0 and q<=50:
    d=q*10

elif q>=51 and q<=60:
    d=500+(q-50)*30
    
elif q>=51 and q<=70:
    d=500+300+(q-60)*40
    
elif q>=51 and q<=80:
    d=500+300+400+(q-70)*50
    
else:
    d=500+300+400+500+(q-80)*60
    
t=q*100

f=t-d

print("Total price is Rs : ",t)
print("Discount price is Rs : ",d)
print("Final payment is Rs : ",f)
