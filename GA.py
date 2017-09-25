import random
from math import sqrt


def Populasi(nPop, kota):
    pop = Kota
    pop = [random.sample(kota, len(kota)) for _ in range(nPop)]
    return pop

def randomPRoute(nPop):
    return int(round(random.uniform(0, nPop)))


def Fitness(route, list_kota):
    distance = 0
    x = list_kota[route[1]].x - list_kota[route[0]].x
    y = list_kota[route[1]].x - list_kota[route[0]].x
    distance += sqrt(x * x + y * y)
    for i in range(len(route)-1):
        if i==range(len(route)):
            x = list_kota[route[0]].x - list_kota[route[i]].x
            y = list_kota[route[0]].x - list_kota[route[i]].x
            distance += sqrt(x * x + y * y)
        else:
            x = list_kota[route[i + 1]].x - list_kota[route[i]].x
            y = list_kota[route[i + 1]].x - list_kota[route[i]].x
            distance += sqrt(x * x + y * y)
    return distance


class Kota:
    def __init__(self, node, x, y):
        self.node = node
        self.x = x
        self.y = y


def inputKota(kota_kota):
    kota0 = Kota(0, 82, 76)
    kota_kota.append(kota0)
    kota1 = Kota(1, 96, 44)
    kota_kota.append(kota1)
    kota2 = Kota(2, 50, 5)
    kota_kota.append(kota2)
    kota3 = Kota(3, 49, 8)
    kota_kota.append(kota3)
    kota4 = Kota(4, 13, 7)
    kota_kota.append(kota4)
    kota5 = Kota(5, 29, 89)
    kota_kota.append(kota5)
    kota6 = Kota(6, 58, 50)
    kota_kota.append(kota6)
    kota7 = Kota(7, 84, 39)
    kota_kota.append(kota7)
    kota8 = Kota(8, 14, 24)
    kota_kota.append(kota8)
    kota9 = Kota(9, 2, 39)
    kota_kota.append(kota9)
    kota10 = Kota(10, 3, 82)
    kota_kota.append(kota10)
    kota11 = Kota(11, 5, 10)
    kota_kota.append(kota11)
    kota12 = Kota(12, 98, 52)
    kota_kota.append(kota12)
    kota13 = Kota(13, 84, 25)
    kota_kota.append(kota13)
    kota14 = Kota(14, 61, 59)
    kota_kota.append(kota14)
    kota15 = Kota(15, 1, 65)
    kota_kota.append(kota15)


if __name__ == '__main__':
    route = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    list_kota = []
    nPop = 853
    nGen = 1
    nKrom = len(route)
    population = []

    bestever = []
    pMutasi = 0.9
    inputKota(list_kota)

    population = Populasi(nPop, route)
    # print population

    for i in range(nGen):
        cRoute = []
        fitness = []
        for _ in range(nPop / 2):
            pRoute1 = randomPRoute(nPop - 1)
            pRoute2 = randomPRoute(nPop - 1)

            cRoute1 = population[pRoute1][:]
            cRoute2 = population[pRoute2][:]

            # mutation
            rand = random.random()
            titik = int(round(random.uniform(0, nKrom - 1)))
            if rand <= pMutasi:
                temp = cRoute1[titik]
                if cRoute1[titik] != 9:
                    cRoute1[titik] = 9
                    for i in range(len(cRoute1)):
                        if cRoute1[i] == 9 and i != titik:
                            cRoute1[i] = temp
                else:
                    cRoute1[titik] = 6
                    for j in range(len(cRoute1) - 1):
                        if cRoute1[j] == 6 and j != titik:
                            cRoute1[j] = temp
            rand = random.random()
            titik = int(round(random.uniform(0, nKrom - 1)))
            if rand <= pMutasi:
                temp = cRoute1[titik]
                if cRoute1[titik] != 9:
                    cRoute1[titik] = 9
                    for i in range(len(cRoute1)):
                        if cRoute1[i] == 9 and i != titik:
                            cRoute1[i] = temp
                else:
                    cRoute1[titik] = 6
                    for j in range(len(cRoute1) - 1):
                        if cRoute1[j] == 6 and j != titik:
                            cRoute1[j] = temp
            rand = random.random()
            titik = int(round(random.uniform(0, nKrom - 1)))
            if rand <= pMutasi:
                temp = cRoute2[titik]
                if cRoute2[titik] != 9:
                    cRoute2[titik] = 9
                    for i in range(len(cRoute2) - 1):
                        if cRoute2[i] == 9 and i != titik:
                            cRoute2[i] = temp
                else:
                    cRoute2[titik] = 6
                    for j in range(len(cRoute2) - 1):
                        if cRoute2[j] == 6 and j != titik:
                            cRoute2[j] = temp
            rand = random.random()
            titik = int(round(random.uniform(0, nKrom - 1)))
            if rand <= pMutasi:
                temp = cRoute2[titik]
                if cRoute2[titik] != 9:
                    cRoute2[titik] = 9
                    for i in range(len(cRoute2) - 1):
                        if cRoute2[i] == 9 and i != titik:
                            cRoute2[i] = temp
                else:
                    cRoute2[titik] = 6
                    for j in range(len(cRoute2) - 1):
                        if cRoute2[j] == 6 and j != titik:
                            cRoute2[j] = temp
            cRoute.append(cRoute1)
            cRoute.append(cRoute2)

            Route = population + cRoute
            for j in range(len(Route)):
                bestever.append(Fitness(Route[j], list_kota))

        # print bestever
        steadyState = sorted(range(len(bestever)), key=lambda k: bestever[k])
        # print Route[steadyState[0]]

        population = []
        for j in range(len(steadyState)):
            population.append(steadyState[j])

    print "Value:", bestever[steadyState[0]]
    # print "Route :",
    # print bestever
    # print Route
