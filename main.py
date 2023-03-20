import Algorithm
import ExcelPlugin

electronicLoad = int(input("Cual es la carga electrica que queires validar? R: "))
# electronsNumber = input("Cual es el numero de electrones? R: ")

algorithm = Algorithm.Colors()
excel = ExcelPlugin.Excel()

result = algorithm.calculate_combinations(electronicLoad)
for electron in result:
    algorithm.combination_sums(electron)
algorithm.print_combinations(result)

y = range(int(algorithm.extremo_inferior_half), int(algorithm.extremo_superior_half)+1)
x = range(int(algorithm.extremo_inferior_value), int(algorithm.extremo_superior_value)+1)

print(list(x))
print(list(y))

excel.set_file()
