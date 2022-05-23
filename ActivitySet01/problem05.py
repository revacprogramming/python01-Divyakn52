# Functions


def computepay(h, r):
    if h<= 40:
        Pay = (h*r)
    elif h>40:
        Pay=(40*r+(h-40)*1.5*r)
    return Pay
hrs=float(input("enter hours:"))
rate=float(input("enter rate:"))
p=computepay(hrs,rate)
print("Pay",p)
