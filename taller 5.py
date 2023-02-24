from scipy.special import factorial
import math

angulo=float(input("Ingrese el valor del angulo en radianes: "))

n = 1
i=0
suma=0
error_esperado = 0.00000001

while abs(n) > error_esperado:
  
  if i % 2 ==0:
    n=1*((angulo**(2*i))/factorial((2*i)))
    i+=1
    suma+=n

    
  else:
    n=-1*((angulo**(2*i))/factorial((2*i)))
    i+=1
    suma+=n
    
    

valor_estimado = suma
error_aproximado = abs((valor_estimado - math.cos(angulo)) / math.cos(angulo)) * 100
print("Valor estimado: {:.8f}".format(valor_estimado))
print("Error aproximado relativo porcentual: {:.8f}%".format(error_aproximado))
print("Número de iteraciones: {}".format(j))
