import Algorithm

electronicLoad = int(input("Cual es la carga electrica que queires validar? R: "))
# electronsNumber = input("Cual es el numero de electrones? R: ")

algorithm = Algorithm.Colors()

result = algorithm.calculate_combinations(electronicLoad)
for electron in result:
    algorithm.combination_sums(electron)
algorithm.print_combinations(result)