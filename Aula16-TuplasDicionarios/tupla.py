carros = "Uno", "Doblo", "Toro", "Jeep"

print(carros[1])
print(carros[1:3])
print(carros[1:])
print(carros[1:-2])

itens = carros[3:], carros[0], 2
print(itens)

def calculcar(x, y):
    return x+y, x-y, x*y, x/4

resultado = calculcar(10, 2)
print("Result: ", resultado)

a, b, c, d = calculcar(9,3)
print("Soma: ", a) 
print("Subtração: ", b) 
print("Multiplicação: ", c) 
print("Divisão: ", d) 