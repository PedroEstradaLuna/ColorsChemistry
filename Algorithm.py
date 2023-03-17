import itertools
from ElectronsDto import Electron

class Colors:
    
    def calculate_combinations(self, electrons_numbers):
        possible_combinations = []

        orbital = ["2⁺","2⁻", "1⁺","1⁻","0⁺","0⁻","-1⁺","-1⁻","-2⁺","-2⁻"] 

        comb_tuples = itertools.combinations(orbital,electrons_numbers)
        count = 0
        for element in comb_tuples:
            comb_list = list(element)
            count += 1
            combination = Electron({'combination':str(comb_list), 'number': count, 'half_sum':0, 'values_sum':0})
            possible_combinations.append(combination)
        return possible_combinations
    
    def print_combinations(self, electron_list):
        for electron in electron_list:
            print('combinacion #',str(electron.number),': ',electron.combination,' Half value: ', electron.half_sum,' Sum value: ', electron.values_sum)
    
    def combination_sums(self,electron):
        values_sum = 0
        half_sum = 0

        values = electron.combination[1 : -1].split(',')
        for value in values:
            value = value[1 : -1]
            print(value)
            if value[-1] == "⁺":
                half_sum += 0.5
            else:
                half_sum += -0.5
                
            electron.half_sum = half_sum
            print(value[:-1])
            only_num = int(value[:-1]) 
            values_sum += only_num
            electron.values_sum = values_sum
        
        electron.combination = ",".join(electron.combination)
    
