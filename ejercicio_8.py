#Fabrica de computadoras

precio = 11000
total = 0
subtot = 0
canti_compus = 1

print ("Digite la cantidad de computadoras que adquirio: ")
canti_compus = int(input())

if canti_compus >= 1: 
    subtot = precio*canti_compus
    descuento = subtot*0.1
    total = subtot-descuento

    if canti_compus < 5:
        subtot = precio*canti_compus
        descuento = subtot*0.1
        total = subtot-descuento
    
    if canti_compus >= 5:
        subtot = precio*canti_compus
        descuento = subtot*0.2
        total = subtot-descuento

    if canti_compus < 10:
        subtot = precio*canti_compus
        descuento = subtot*0.2
        total = subtot-descuento
    
    if canti_compus >= 10:
        subtot = precio*canti_compus
        descuento = subtot*0.4
        total = subtot-descuento
    
    print ("El total de la compra es: $",total)

else:
    print ("Error")

print ("Lindo dia!")