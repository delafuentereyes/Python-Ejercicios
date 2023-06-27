#Compra en el super con numero al azar

total = 0
monto = 1

import random

intentos = 0
numero_adivinar = random.randint(0,100)

print ("Digite el monto que le están cobrando: ")
monto = int(input())
print ("--------------------------------------------------")

while intentos < 10:
    intentos = intentos + 1
    print ("Digite un numero al azar: ")
    num = int(input())

    if numero_adivinar == num:
        print ("Felicidades, acertó el número!!")
        break

    if num == numero_adivinar < 80:
        descuento = monto*0.15
        total = monto-descuento
    else:
        total = monto

    if num == numero_adivinar >= 80:
        descuento = monto*0.2
        total = monto-descuento
    else:
        total = monto

if num == numero_adivinar:
    print ("Ganó!!")
else:
    print ("Mala suerte, el numero era: ",numero_adivinar)

print ("El monto a pagar es: ",total)

