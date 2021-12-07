#condicional if

dato=int(input("ingrese un numero: "))

if dato>0:
    print("numero positivo")
    print("segundo resultado positivo")   
elif dato==0:
    print("resultado 0")
else:
    print("es negativo")
    
print("fin")

#ejercicio 1
#pide 2 num y obtener par

n1=int(input("ingrese un numero: "))
n2=int(input("ingrese otro numero: "))

if n1%2==0 and n2%2==0:
    print("ambos son pares")
elif n1%2==0 and n2%2!=0:
    print(f"{n1} es un numero par")
elif n1%2!=0 and n2%2==0:
    print(f"{n2} es un numero par")
else:   
    print("los dos numeros son impares")
    
#ejercicio 2
#pedir 3 num. y devolver el mayor

n1=int(input("ingrese el numero: "))
n2=int(input("ingrese el numero: "))
n3=int(input("ingrese el numero: "))

if n1>=n2 and n1>=n3:
    print("el numero mayor es: {n1}")
elif n2>=n1 and n2>=n3:
    print("el numero mayor es: {n2}")
elif n3>=n1 and n3>=n2:
    print("el numero mayor es: {n3}")
    
#ejercicio 3
#compara dos nombres y verifica si hay coincidencias 

nombre1=input("ingrese nombre 1: ")
nombre2=input("ingrese nombre 2: ")


if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    print("Si hay coincidencia")
else:
    print("No hay coincidencia")
    
#ejercicio 4
# simulacion de cajero automatico con un saldo inicial de $2000 
#y un menu: 1)ingresode dinero, 2)retirardinero, 3)mostrar dinero, 4)salir

saldo=2000
print("1. Ingresar Dinero")
print("2. Retiro de Dinero")
print("3. Mostrar Dinero")
print("4. Salir")

seleccion = int(input("elija una opcion: "))

if seleccion==1:
    ingreso = float(input("Dinero a Ingresar: "))
    saldo+=ingreso
    print(f"Nuevo saldo en la cuenta: {saldo}")
elif seleccion==2:
    salida = float(input("Dinero de Salida: "))
    if salida>saldo:
      print("saldo insuficiente")
    else:
        saldo-=salida
        print(f"Nuevo saldo disponible {saldo}")
elif seleccion==3:
    print(f"Saldo Disponible: {saldo}")
elif seleccion==4:
    print("fin")
else:
    print("Error de entrada de datos")
    
