# entrada de datos
def main():
    n1=input("ingrese un numero entero: ")
    n2=input("ingrese otro numero entero: ")
    
    for x in range (n1,n2):
      
        print (x*x)
main()

#ejercicio 1

a= float(input("a: "))
b= float(input("b: "))
c= float(input("c: "))

r=((c+5)*(b**2-3*a*c)*a**2)/(4*a)

print(f"La res5puesta es: {r}")

#ejercicio 2

a= input("a: ")
b= input("b: ")
a,b=b,a

print(f"el nuevo valor de a es: {a}")
print(f"el nuevo valor de b es: {b}")

#ejercicio 3
#radio y longitud de un circulo

import math

r=float(input("ingrese el radio: "))
area=math.pi*r**2
longitud=2*math.pi*r

print(f"el area es: {area:.1f}")
print(f"la longitud es: {longitud:.1f}")

#ejercicio 4
#precio final con %36 de descuento

precioinicial=float(input("ingrese el precio: "))
descuento=precioinicial*(36/100)
preciofinal=precioinicial-descuento

print(f"el precio final es: {preciofinal:.2f}")
