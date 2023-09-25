print("Ejercicio 1")

print("Desea ingresar a la calculadora?")
print("1: si")
print("2: no")


o=input("Ingrese una opcion")
o=int(o)
while o==1:

   

    x=input("Ingrese su primer numero")
    y=input("Ingrese su segundo numero")
    x=int(x)
    y=int(y)

    print("1: suma")
    print("2: resta")
    print("3: multiplicacion")
    print("4: division")
    print("5: modulo")
    print("6: exponente")
    print("7: cociente")
    print("8: salir")
    z=input("Ingrese una opcion")
    z=int(z)

    sum=x+y
    res=x-y
    mul=x*y
    div=x/y
    mod=x%y
    exp=x**y
    coc=x//y




    

    if z==1:
        print(str(x)+"+"+str(y)+"="+ str(sum))

    elif z==2:
        print(str(x)+"-"+str(y)+"="+ str(res))

    elif z==3:
        print(str(x)+"*"+str(y)+"="+ str(mul))

    elif z==4:
        print(str(x)+"/"+str(y)+"="+ str(div))

    elif z==5:
        print(str(x)+"%"+str(y)+"="+ str(mod))

    elif z==6:
        print(str(x)+"**"+str(y)+"="+ str(exp))

    elif z==7:
        print(str(x)+"//"+str(y)+"="+ str(coc))

    elif z==8:
        print("adios")
        break
    else:
        print("Esta opcion no es válida")