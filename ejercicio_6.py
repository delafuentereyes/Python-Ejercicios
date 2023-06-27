#Sumatoria de numeros pares
total = 0
num = 0
num = int(input("Digite su numero limite: "))
lista = []

for n in range (0, num + 1): 
    if n % 2 == 0:
        lista.append(n) 
        total += n

print ("Los numeros pares son: ",lista)
print ("La sumatoria de esos numeros es: ",total)