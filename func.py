def menorNaoVisit(matAdj, u, naoVisitados):
    min = 500000

    for i in range(len(matAdj)):
        if matAdj[u][i] < min and i in naoVisitados:
            min = matAdj[u][i]
            vertMin = i

    return vertMin

def nearestneighbor(matAdj):
    naoVisitados = [x for x in range(len(matAdj))]
    s = []

    u = 0
    s.append(u)
    while len(naoVisitados) != 0:
        v = menorNaoVisit(matAdj, u, naoVisitados)
        print(s)
        s.append(v)
        naoVisitados.remove(v)
        u = v
    s.append(s[0])
    return s