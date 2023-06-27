#Compra en una tienda
cantida_gastada = 1
total = 0

print ("Digite la cantidad que gastó en el supermercado: ")
cantida_gastada = float(input())

if cantida_gastada > 10000:
    descuento = cantida_gastada*0.10
    total = cantida_gastada-descuento

    if cantida_gastada < 20000:
        descuento = cantida_gastada*0.10
        total = cantida_gastada-descuento

    if cantida_gastada > 20001:
        descuento = cantida_gastada*0.30
        total = cantida_gastada-descuento


    if cantida_gastada <= 50000:
        descuento = cantida_gastada*0.30
        total = cantida_gastada-descuento

    if cantida_gastada > 50000:
        descuento = cantida_gastada*0.50
        total = cantida_gastada-descuento
        
    print ("El total de la compra es: ",total)

else:
    print ("A la cantidad que digitó no se le puede aplicar descuento")

print ("Fin de la compra, buen dia!")



