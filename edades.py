edad = int(input("ingresa tu edad : "))

if edad < 1 or edad > 125:
    resultado = "Edad invalida"
   
elif 18 <= edad <= 59:
    resultado = "Eres mayor de edad"

elif edad < 18  :
    resultado = "Menor de edad"

else:
    resultado = "De la tercera edad"

print(resultado)


