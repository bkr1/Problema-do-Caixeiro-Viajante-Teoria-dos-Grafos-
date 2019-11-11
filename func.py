import random
import time

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
    naoVisitados.remove(0)
    while len(naoVisitados) != 0:
        v = menorNaoVisit(matAdj, u, naoVisitados)
        #print(s)
        s.append(v)
        naoVisitados.remove(v)
        u = v
    s.append(s[0])
    return s

def twoopt(matAdj, s):
    tempoFim = time.time() + 60
    b = 0
    for i in range(len(s)):
        b += 1
    
    b -= 1
    print("Processando...")
    while time.time() < tempoFim:
        i1 = random.randint(0, b)
        i2 = random.randint(0, b)

        if i1 != i2:
            s2 = s
            s[i1] = s2[i2]
            s2[i2] = s[i1]

            if avalia(s2, matAdj) < avalia(s, matAdj):
                s = s2.copy
    return s


def avalia(s, matAdj):
    custo = 0
    for i in range(len(s) - 1):
        u = s[i]
        v = s[i + 1]
        custo += matAdj[u][v]
    return custo