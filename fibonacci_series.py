def fib():
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))
    n = int(imput("enter the range:"))
    c = a + b
    count = 0
    while count+2 < n:
        c = a+b
        a=b
        b=c
        count += 1
        print(c)
x = fib()
print(x)
  
