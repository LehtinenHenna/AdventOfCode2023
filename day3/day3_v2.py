import sys
sys.path.append('..\\utils')
from util import file_reader



class EnginePartNumberAdder:
    '''
    Uses puzzle input path to find engine part numbers that are touching a symbol and sums them together.
    This solution is currently bugged, as it doesn't take into consideration lines that end in a number,
    e.g. '..*34...24'
    '''
    def __init__(self, puzzle_input_path):
        self.puzzle_input_path = puzzle_input_path # filepath to puzzle input
        self.engine_part_sum = 0

    def find_symbol(self, line, previous_line, next_line, digit_indexes):
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
        # compare with indexes from past row and next row
        for i in range(digit_indexes[0] - 1, digit_indexes[-1] + 2):
            if not previous_line[i].isdigit() and previous_line[i] != '.':
                symbol_found = True
            if not next_line[i].isdigit() and next_line[i] != '.':
                symbol_found = True
        return symbol_found

    def add_engine_part_numbers(self):
        file_content = file_reader(self.puzzle_input_path).splitlines()
        for line_index, line in enumerate(file_content):
            print('line', line)
            digit_indexes = []
            for index, character in enumerate(line):
                #print('index, character', index, character)
                if character.isdigit():
                    #print('character is digit', character)
                    # Append index to digit_indexes for later processing.
                    digit_indexes.append(index)
                elif not character.isdigit():
                        if digit_indexes:
                            #print('we just stepped out of a number at index', index, 'character', character)
                            # A number was found in the previous indexes, find out if a symbol is touching it.
                            mock_line = len(line) * '.'
                            if line_index == len(file_content) - 1:
                                # last line
                                symbol_found = self.find_symbol(line, file_content[line_index - 1], mock_line, digit_indexes)
                            elif line_index == 0:
                                # first line
                                symbol_found = self.find_symbol(line, mock_line, file_content[line_index + 1], digit_indexes)
                            else:
                                symbol_found = self.find_symbol(line, file_content[line_index - 1], file_content[line_index + 1],  digit_indexes)
                            # construct the number
                            number = ''
                            for i in digit_indexes:
                                number += line[i]
                            if symbol_found:
                                print('symbol was found for number', line[digit_indexes[0]:digit_indexes[-1]+1])
                                # add number to the engine part sum
                                self.engine_part_sum += int(number)
                                print('self.engine_part_sum', self.engine_part_sum)
                            digit_indexes = []

        return self.engine_part_sum
        
if __name__ == '__main__':
    engine_part_number_adder = EnginePartNumberAdder('test-input.txt')
    engine_part_sum = engine_part_number_adder.add_engine_part_numbers()
    print('engine_part_sum', engine_part_sum)