print("1. factorial")
print("2. Secuencia de Fibonacci")
print("3. salir")
x= input()
x= input(x)

ifx=1
print("ingrese un numero")
n1= input()
n1=int(n1)
factorial=n1

for i in range(1,n1+1):
    factorial=i*factorial
    print(str(n1)+"...*2*1="+str(factorial))