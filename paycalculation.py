def computepay(h,r):
    if h>40:
        pay = 40*r + (h-40)*(1.5*r)
    else:
        pay = h*r
    return pay

hrs = input("Enter Hours:")
pay = input("Enter Pay:")
p = computepay(float(hrs),float(pay))
print("Pay", p)
