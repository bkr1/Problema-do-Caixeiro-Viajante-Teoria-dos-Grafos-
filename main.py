import os
import func

global matAdj
global listaAdj
global vertices
global arestas

def mainf():
    os.system("cls")
    print("\t---------- PROBLEMA DO CAIXEIRO VIAJANTE ----------\n")
    print("\n\t1.   Usar grafo de teste (toy.txt);" + "\n\t2.   Inserir grafo;" +
         "\n\t3.   Sair.")

    op = int(input("\nDigite sua opcao: "))

    if(op == 1):
        preenche("toy.txt")
    elif(op == 2):
        nome = input("\nInforme o nome do arquivo (.txt): ")
        preenche(nome)
    else:
        os.system("cls")
        exit()


def preenche(nome):
    global matAdj
    global listaAdj
    global vertices
    global arestas

    fileName = nome
    file = open(fileName)

    str = file.readline()
    str = str.split(" ")

    numVertices = int(str[0])
    numArestas = int(str[1])

    listaAdj = [[]for x in range(numVertices)]
    matAdj = [[0 for x in range(numVertices)] for x in range(numVertices)]

    vertices = [x for x in range(numVertices)]
    arestas = []

    for i in range(numArestas):
        str = file.readline()
        str = str.split(" ")
        origem = int(str[0])
        destino = int(str[1])
        peso = int(str[2])
        listaAdj[origem].append((destino, peso))
        matAdj[origem][destino] = peso
        arestas.append((origem, destino, peso))
    mainMenu()

def mainMenu():
    os.system("cls")

    op = 0
    while True:
        if op != 3:
            print("\t---------- PROBLEMA DO CAIXEIRO VIAJANTE ----------\n")
            print("\n\t1.   Algoritmo do Nearest Neighbor;" + "\n\t2.   Algoritmo de Twoopt." +
                 "\n\t3.   Sair.")
            op = int(input("\nDigite sua opcao: "))
        if op == 3:
            mainf()
        if op == 2:
            os.system("cls")
            print("work in progress...")
            os.system("pause")
        if op == 1:
            os.system("cls")

            s = func.nearestneighbor(matAdj)
            print(s)

            os.system("pause")
            os.system("cls")
            

mainf()