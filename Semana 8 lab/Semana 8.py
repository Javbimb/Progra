while True:
    print("1. factorial")
    print("2. Secuencia de Fibonacci")
    print("3. salir")
    o= input()
    o= int(o)

    if o==1:
     print("ingrese un numero")
    n1= input()
    n1=int(n1)
    factorial=n1

    for i in range(1,n1+1):
        factorial=i*factorial
    print(str(n1)+"...*2*1="+str(factorial))

    if o == 2:
        x=0
        y=1
        z=0
        print("ingrese un numero")
        n2=input(":")
        n2=int(n2)

        print(str(x)+", "+str(y)+", ",end=" ") 
        for s in range(0,n2):
         z=x+y
        print(str(z)+", ",end=" ") 
        x=y
        y=z
        print("Fibonacci: ("+str(n2)+")")
    if o == 3:
     break