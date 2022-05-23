# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rate= input("enter rate:")
r=float(rate)
if h>40 :
    print(r*40+(h-40)*1.5*r)
else:
    pay=h*r
    print(pay)
    
