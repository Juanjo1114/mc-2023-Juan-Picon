A=set()
B=set()
 
print("ingrese un número para agregar al conjunto, si desea continuar al siguiente deje el espacio vacio")
print("CONJUNTO A: ")

while True:

    x=input("Digite un elemento del conjunto A: ")
    if (x==""):
        break

    A.add(float(x))
    
print("CONJUNTO B: ")
while True:
    x=input("Digite un elemento del conjunto B: ")
    if (x==""):
        break
    B.add(float(x))

print("Conjunto A: ", A) 
print("Conjunto B: ", B)

        
opciones=int(input("A continuación se le darán las opciones que puede realizar con el programa, seleccione uno de los números con la acción a realizar.\n 1. Unión \n 2. Intersección \n 3. Diferencia \n 4. Diferencia simétrica"))
if (opciones==1):
    print("La unión de A y B es: ", A|B)
elif (opciones==2):
    print("La intersección de A y B es: ", A&B)
elif(opciones==3):
    print("La diferencia de A y B es: ", A-B)
elif(opciones==4):
    print("La diferencia simétrica de A y B es: ", A^B)
        


