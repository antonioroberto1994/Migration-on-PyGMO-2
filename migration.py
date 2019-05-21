import pygmo as pg

def chainMigration(archi):
    nIsl = len(archi)

    bestIdx = []
    worstIdx = []

    for i in range(nIsl):
        popI = archi[i].get_population()
        bestIdx.append(popI.best_idx())
        worstIdx.append(popI.worst_idx())

    for i in range(nIsl-1):
        next = i+1
        popI = archi[i].get_population()
        popNext = archi[next].get_population()
        popNext.set_x(worstIdx[next], popI.get_x()[bestIdx[i]])
        archi[next].set_population(popNext)

def ringMigration(archi, plusOne=False):
    nIsl = len(archi)

    bestIdx = []
    worstIdx = []

    for i in range(nIsl):
        popI = archi[i].get_population()
        bestIdx.append(popI.best_idx())
        worstIdx.append(popI.worst_idx())

    for i in range(nIsl):
        next = (i+1) % nIsl
        popI = archi[i].get_population()
        popNext = archi[next].get_population()
        popNext.set_x(worstIdx[next], popI.get_x()[bestIdx[i]])
        worstIdx[next] = popNext.worst_idx()
        archi[next].set_population(popNext)
        if plusOne:
            next = (next+1) % nIsl
            popNext = archi[next].get_population()
            popNext.set_x(worstIdx[next], popI.get_x()[bestIdx[i]])
            worstIdx[next] = popNext.worst_idx()
            archi[next].set_population(popNext)
