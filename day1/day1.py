import sys
sys.path.append('..\\utils')
#import util
from util import file_reader, file_line_reader

class DigitSum:
    '''
    Uses self.parse_digits method to read a text file line by line.
    collects each digit and number word converted to digit (e.g., "seven" as "7") from each line.
    Extracts a joint number from each line consisting of the first and last number found on that line.
    E.g. "twoxjzgsjzfhzhm1" results in 21 and "xcsfkjqvln2tpm" results in 22.
    Adds each number found this way to a total sum.
    '''
    def __init__(self, puzzle_input_path):
        self.puzzle_input_path = puzzle_input_path
        self.puzzle_input = ""
        self.total_sum = 0
        self.number_conversion_table = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }

    def find_digits(self):
        for line in file_line_reader(self.puzzle_input_path):
            digits = []
            for i, character in enumerate(line):
                # append digits
                if character.isdigit():
                    digits.append(character)
                else:
                    # loop through characters in sets of 5, looking for number words in the beginning of each substring
                    # append the digit equivalent of the number word to digits, e.g. "eight" as "8"
                    for key, value in self.number_conversion_table.items():
                        print('line[i:i+5]', line[i:i+5], 'key', key)
                        if line[i:i+5].startswith(key):
                            digits.append(value)
            # extract the first and last digit to form a number, e.g. from [1, 2, 3] to integer 13
            number_to_add = int("{}{}".format(digits[0], digits[-1]))
            # add the extracted integer to the total sum
            self.total_sum += number_to_add
        return self.total_sum
        

if __name__ == '__main__':
    parser = DigitSum('test-input.txt')
    summed = parser.find_digits()
    print('sum', summed)