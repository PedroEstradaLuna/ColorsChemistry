import itertools

def setFormat(combinacion):
    if combinacion == 1:
        return 2
    if combinacion == 2:
        return 1
    if combinacion == 3:
        return 0
    if combinacion == 4:
        return -1
    if combinacion == 5:
        return -2    

print("Programa para hacer la tarea de la poncha")

tresPalitos = [1,2]
cuatroPalitos = [[2,2],[1,1,2]]
listaChida = []

espacios = [1,2,3,4,5]
longitud = 2
combinacionesDobles = list(itertools.permutations(espacios, longitud))
#print(combinacionesDobles)
finalTres = []
valores = ['+','-']
for combinacion in combinacionesDobles:
    for valor in valores:
        aux = []
        aux.append(setFormat(combinacion[0]))
        aux.append(setFormat(combinacion[1]))
        aux.append(setFormat(combinacion[1]))
        finalTres.append(aux)


longitud = 3
combinacionTriples = list(itertools.combinations(espacios, longitud))
#print(combinacionTriples)
for combinacion in combinacionTriples:
    for valor in valores:
        aux = []
        aux.append(setFormat(combinacion[0]))
        aux.append(setFormat(valores[0] + combinacion[1]))
        aux.append(setFormat(combinacion[2]))
        finalTres.append(aux)

#combinacionTriplesVariadas =[[0.5,0.5,-0.5],[0.5,-0.5,0.5],[0.5,-0.5,-0.5]]

#for variadas in combinacionTriplesVariadas:
#    products = list(itertools.product(x, y))

#for i in finalTres:
#    print(i)

print(finalTres)
print('########################################################')
x3 = []
for element in finalTres:
    aux = []

    aux.append(element[0])
    aux.append(element[1] * -1)
    aux.append(element[2] * -1)
    x3.append(aux)

print(x3)