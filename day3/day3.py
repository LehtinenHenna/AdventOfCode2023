import sys
sys.path.append('..\\utils')
from util import file_line_reader



class EnginePartNumberAdder:
    '''Uses puzzle input path to find engine part numbers that are touching a symbol and sums them together'''
    def __init__(self, puzzle_input_path):
        self.puzzle_input_path = puzzle_input_path # filepath to puzzle input
        self.current_row_numbers_without_symbol = {} # key =  number as string, value = list of indexes
        self.past_row_numbers_without_symbol = {} # key =  number as string, value = list of indexes
        self.current_row_symbols = [] # list of indexes of symbols from the current row of puzzle input
        self.past_row_symbols = [] # list of indexes of symbols from the previous row of puzzle input
        self.engine_part_sum = 0

    def find_symbol(self, line, digit_indexes):
        '''
        Find if there's a symbol on either side of the number or 
        If a symbol from the previous line touches the number.
        '''
        print('trying to find a symbol for found number ', line[digit_indexes[0]:digit_indexes[-1]+1])
        symbol_found = False
        # check character before number
        if line[digit_indexes[0] - 1] != '.':
            symbol_found = True
        # check character after number
        elif line[digit_indexes[-1] + 1] != '.':
            symbol_found = True
        # compare with symbols from past row
        for i in range(digit_indexes[0] - 1, digit_indexes[-1] + 2):
            if i in self.past_row_symbols:
                symbol_found = True
        return symbol_found
        

    def add_engine_part_numbers(self):
        '''
        Finds relevant engine part numbers and sums them together.
        '''
        for line in file_line_reader(self.puzzle_input_path):
            digit_indexes = []
            print('line', line)

            for index, character in enumerate(line):
                #print('index, character', index, character)
                if character.isdigit():
                    #print('character is digit', character)
                    # Character is a digit.
                    # Append index to digit_indexes for later processing.
                    digit_indexes.append(index)

                elif not character.isdigit():
                    if digit_indexes:
                        #print('we just stepped out of a number at index', index, 'character', character)
                        # A number was found in the previous indexes, find out if a symbol is touching it.
                        symbol_found = self.find_symbol(line, digit_indexes)
                        # construct the number
                        number = ''
                        for i in digit_indexes:
                            number += line[i]
                        if symbol_found:
                            print('symbol was found for number', line[digit_indexes[0]:digit_indexes[-1]+1])
                            # add number to the engine part sum
                            self.engine_part_sum += int(number)
                            print('self.engine_part_sum', self.engine_part_sum)
                        else:
                            # If no symbol is found, save the number with start index to self.current_row_numbers_without_symbol.
                            self.current_row_numbers_without_symbol[number] = digit_indexes
                        digit_indexes = []

                    if character != '.':
                        # Character is a symbol. 
                        # Save the symbols to self.current_row_symbols for the next round.
                        self.current_row_symbols.append(index)
                        # Check if one of the numbers from the previous row has a matching index.
                        for number_str, i_list in self.past_row_numbers_without_symbol.items():
                            print('trying to find a symbol for past row number', number_str, 'with current character', character)
                            add_number = False
                            for i in range(i_list[0] - 1, i_list[-1] + 2):
                                if index == i:
                                    add_number = True
                            if add_number:
                                print('symbol was found for past row number', number_str)
                                self.engine_part_sum += int(number_str)
                                print('self.engine_part_sum', self.engine_part_sum)
                                
            self.past_row_numbers_without_symbol = self.current_row_numbers_without_symbol.copy()
            self.current_row_numbers_without_symbol = {}
            self.past_row_symbols = self.current_row_symbols.copy()
            self.current_row_symbols = []
        return self.engine_part_sum
    
if __name__ == '__main__':
    engine_part_number_adder = EnginePartNumberAdder('puzzle-input3.txt')
    engine_part_sum = engine_part_number_adder.add_engine_part_numbers()
    print('engine_part_sum', engine_part_sum)