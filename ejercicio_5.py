#Sumatoria de numeros
y = 1
sumatoria = 0
n = int(input("Digite el número: ")) 

while y <= n:
    sumatoria += y
    y += 1 

print ("El valor de la sumatoria es: ",sumatoria)