# Alexandro Aguilar NC = 0007
# 2 Ejemplos por caso

# Caso 1: if, elif y else
print("+-+-+-+-+ Ejemplos de if +-+-+-+-+-+")
# Ejemplo 1
compra = 120
if compra > 100:
    print("¡Tienes un 10% de descuento!")

# Ejemplo 2
semaforo = "verde"

if semaforo == "verde":
    print("Puedes avanzar.")

print("+-+-+-+-+ Ejemplos de else +-+-+-+-+-+")
# Ejemplo 2 
numero = 7

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

#Ejemplo 2
usuario_conectado = False

if usuario_conectado:
    print("Bienvenido a tu panel.")
else:
    print("Por favor, inicia sesión.")

print("+-+-+-+-+ Ejemplos de elif +-+-+-+-+-+")
bateria = 15

if bateria > 20:
    print("Batería suficiente.")
elif bateria <= 15:
    print("Modo de ahorro de energía activado.")

# Ejemplo 2
ruedas = 2

if ruedas == 4:
    print("Es un auto.")
elif ruedas == 2:
    print("Es una motocicleta.")

# Caso 2: for y while
print("+-+-+-+-+ Ejemplos de for  +-+-+-+-+-+")
# Ejemplo 1
for i in range(1, 6):
    print(f"Número: {i}")
# Ejemplo 2
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(f"Me gusta la {fruta}")

print("+-+-+-+-+ Ejemplos de While  +-+-+-+-+-+")
# Ejemplo 1
contador = 3

while contador > 0:
    print(f"Conteo: {contador}")
    contador -= 1  # Resta 1 en cada iteración

print("¡Despegue!")

# Ejemplo 2
porcentaje = 0

while porcentaje < 100:
    porcentaje += 25  # Suma 25 en cada iteración
    print(f"Cargando... {porcentaje}%")

print("¡Descarga completa!")

print("Programa realizado por Alexandro Aguilar")