import random
import time
import os

def menorNaoVisit(matAdj, u, naoVisitados):
    min = 500000

    for v in range(len(matAdj)):
        if matAdj[u][v] != 0 and matAdj[u][v] < min and v in naoVisitados:
            min = matAdj[u][v]
            vertMin = v
    return vertMin

def nearestneighbor(matAdj):
    naoVisitados = [x for x in range(len(matAdj))]
    s = []

    u = 0
    s.append(u)
    naoVisitados.remove(u)
    while len(naoVisitados) != 0:
        v = menorNaoVisit(matAdj, u, naoVisitados)
        #print(s)
        s.append(v)
        naoVisitados.remove(v)
        u = v
    s.append(s[0])
    print("Distância Nearest Neighbor: " + str(avalia(s, matAdj)))
    return s

def twoopt(matAdj, s):
    tempoFim = time.time() + 60
    
    print("Processando...")
    while time.time() < tempoFim:
        i1 = random.randint(1, len(s) - 2)
        i2 = random.randint(1, len(s) - 2)

        if i1 != i2:
            s2 = s.copy()

            aux = s2[i1]
            s2[i1] = s2[i2]
            s2[i2] = aux

            if avalia(s2, matAdj) < avalia(s, matAdj):
                s = s2.copy()
    print("Distância pós 2 Opt.: " + str(avalia(s, matAdj)))
    return s


def avalia(s, matAdj):
    custo = 0
    for i in range(len(s) - 1):
        u = s[i]
        v = s[i + 1]
        custo += matAdj[u][v]
    return custo