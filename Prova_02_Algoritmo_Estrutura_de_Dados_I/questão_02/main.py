"""
Construa um software em Python que implemente uma Fila de carros e uma Fila de drones.

As classes Carro e Drone herdam da classe veículo os atributos e comuns às duas classes.

A classe carro é composta dos atributos marca, modelo e portas. O atributo portas é fracamente privado.

A classe drone é composta dos atributos marca, modelo e quantidade de hélices. O atributo quantidade de hélices é fortemente privado.

Todas classes devem ter um método para imprimir as informações dos seus respectivos atributos.

Implemente uma tela com um menu (funcionando) que permita ao usuário:

-> Adicionar e remover carros da Fila.

-> Adicionar e remover drones da Fila.

-> Imprimir a Fila de carros e a Fila de drones.

Cole todo código desenvolvido, em sequência, separando as classes por uma linha.
"""

from Drone import Drone
from Carro import Carro
from FilaCarros import FilaCarros
from FilaDrones import FilaDrones

c1 = Carro("Chevrolet", "Camaro", "2")
c2 = Carro("Fiat", "Uno", "4")
c3 = Carro("Toyota", "Corolla", "4")

d1 = Drone("NaoSei", "Modelo1", "8")
d2 = Drone("SeiNao", "RTX", "6")
d3 = Drone("Drone111", "XLS", "12")

# print(c1)
# print("---------")
# print(c2)
# print("---------")
# print(d1)
# print("---------")
# print(d2)
# print("*************")

filaCarros = FilaCarros()
filaDrones = FilaDrones()

# filaCarros.add(c1)
# filaCarros.add(c2)
# filaCarros.add(c3)
# filaCarros.remover()
# print("-------------")
# filaDrones.add(d1)
# filaDrones.add(d2)
# filaDrones.add(d3)
# filaDrones.remover()


# menu = input("""
# MENU
# 1. Carro
# 2. Drone
# """)
# if menu == 1:
#     menuCarro = input("""
#     1. Adicionar Carro
#     2. Remover Carro
#     """)
#     if menuCarro == 1:
#         marca = input("Marca do carro: ")
#         modelo = input("Qual o modelo do carro: ")
#         portas = input("Quantidade de portas: ")
#         addCarro = [marca, modelo, portas]
#         filaCarros.add(addCarro)
#     else:
#         remCarro = ("Qual carro você deseja remover: ")
#         filaCarros.remover(remCarro)
# else:
#     menuDrone = input("""
# 1. Adicionar Drone
# 2. Remover Drone
# """)

# if adicionar:
#     filaCarros.add(carro)
while True:
    menu = int(input("""
        MENU
        1. Adicionar Carro
        2. Remover Carro
        3. Adicionar Drone
        4. Remover Drone
        5. Imprimir fila de carros
        6. Imprimir fila de drones
        """))
    if menu == 1:
        marca = input("Marca do carro: ")
        modelo = input("Qual o modelo do carro: ")
        portas = input("Quantidade de portas: ")
        carro = Carro(marca, modelo, portas)
        filaCarros.add(carro)
    elif menu == 2:
        remCarro = ("Qual carro você deseja remover: ")
        filaCarros.remover()
    elif menu == 3:
        marca = input("Marca do drone: ")
        modelo = input("Qual o modelo do drone: ")
        qtdH = input("Quantidade de helices: ")
        drone = Carro(marca, modelo, qtdH)
        filaDrones.add(drone)
    elif menu == 4:
        remDrone = ("Qual drone você deseja remover: ")
        filaCarros.remover()
    elif menu == 5:
        filaCarros.imprimir()
    elif menu == 6:
        filaDrones.imprimir()
    SimNao = input("Você deseja continuar S/N: ")
    if SimNao == "S" or "s":
        continue
    else:
        break