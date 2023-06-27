#Calculo de salario
salario_hora = 5500
dia_semana = 1
horas_dia = 0
sueldo = 0

while dia_semana <= 6:
    
    print("Digite las horas del dia ", dia_semana)
    dia_semana = dia_semana + 1
    horas_dia = int(input())
    sueldo = sueldo + (horas_dia * salario_hora)
    sueldo = sueldo-0.25 

print("El sueldo del trabajador con el rebajo de pension y salud es de: ",sueldo)