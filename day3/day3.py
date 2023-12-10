import sys
sys.path.append('..\\utils')
from util import file_line_reader



class EnginePartNumberAdder:
    '''
    Uses puzzle input path to find engine part numbers that are touching a symbol and sums them together.
    The whole assignment description can be found in assignment3.md.
    '''
    def __init__(self, puzzle_input_path):
        self.puzzle_input_path = puzzle_input_path # filepath to puzzle input
        self.current_line_numbers_without_symbol = {} # key = number as string, value = list of indexes for the number string
        self.past_line_numbers_without_symbol = {} # key = number as string, value = list of indexes for the number string
        self.current_line_symbols = [] # list of indexes of symbols from the current line of puzzle input
        self.past_line_symbols = [] # list of indexes of symbols from the previous line of puzzle input
        self.engine_part_sum = 0

    def find_symbol(self, line, digit_indexes):
        '''
        Find if there's a symbol on either side of the number or 
        If a symbol from the previous line touches the number.
        '''
        #print('trying to find a symbol for found number ', line[digit_indexes[0]:digit_indexes[-1]+1])
        symbol_found = False
        # check character before number
        if digit_indexes[0] != 0:
            if line[digit_indexes[0] - 1] != '.':
                symbol_found = True
        # check character after number
        if digit_indexes[-1] != len(line) - 1:
            if line[digit_indexes[-1] + 1] != '.':
                symbol_found = True
        # compare with symbols from past line
        for i in range(digit_indexes[0] - 1, digit_indexes[-1] + 2):
            if i in self.past_line_symbols:
                symbol_found = True
        return symbol_found

    def process_found_number(self, line, digit_indexes):
        '''A number was found in the previous indexes, find out if a symbol is touching it.'''
        symbol_found = self.find_symbol(line, digit_indexes)
        # construct the number
        number = ''
        for i in digit_indexes:
            number += line[i]
        if symbol_found:
            #print('symbol was found for number', line[digit_indexes[0]:digit_indexes[-1]+1])
            # add number to the engine part sum
            self.engine_part_sum += int(number)
            #print('self.engine_part_sum', self.engine_part_sum)
        else:
            # If no symbol is found, save the number with its indexes to self.current_line_numbers_without_symbol.
            self.current_line_numbers_without_symbol[number] = digit_indexes

    def add_engine_part_numbers(self):
        '''
        Finds relevant engine part numbers and sums them together.
        '''
        digit_indexes = []
        for line in file_line_reader(self.puzzle_input_path):
            #print('line', line)

            for index, character in enumerate(line):
                #print('index, character', index, character)
                if character.isdigit():
                    # Append index to digit_indexes for later processing.
                    digit_indexes.append(index)

                elif not character.isdigit():
                    
                    if digit_indexes:
                        # When finding a character that is not a number, process any number that may have been in the previous indexes.
                        # e.g., if the line is '...224.' and we're at the last '.', process number '224'
                        self.process_found_number(line, digit_indexes)
                        digit_indexes = []

                    if character != '.':
                        # Character is a symbol. 
                        # Save the symbol to self.current_line_symbols so that it can be compared to numbers in the next line.
                        self.current_line_symbols.append(index)
                        # See if the symbol is touching one of the numbers from the previous line that hadn't found a touching symbol previously.
                        for number_str, i_list in self.past_line_numbers_without_symbol.items():
                            #print('trying to find a symbol for past line number', number_str, 'with current character', character)
                            match_found = False
                            for i in range(i_list[0] - 1, i_list[-1] + 2):
                                if index == i:
                                    match_found = True
                            if match_found:
                                #print('symbol was found for past line number', number_str)
                                self.engine_part_sum += int(number_str)
                                #print('self.engine_part_sum', self.engine_part_sum)

            # process number at the end of the line before going to the next line
            # fixes cases where line ends in number e.g. '....45'
            if digit_indexes:       
                self.process_found_number(line, digit_indexes)
                digit_indexes = []
                
            # At the end of the line, move current line numbers without symbol and current line symbols as previous line equivalents. 
            # Empty current line numbers without symbol and current line symbols.
            self.past_line_numbers_without_symbol = self.current_line_numbers_without_symbol
            self.current_line_numbers_without_symbol = {}
            self.past_line_symbols = self.current_line_symbols
            self.current_line_symbols = []

        return self.engine_part_sum
    
if __name__ == '__main__':
    engine_part_number_adder = EnginePartNumberAdder('puzzle-input3.txt')
    engine_part_sum = engine_part_number_adder.add_engine_part_numbers()
    print('engine_part_sum', engine_part_sum)