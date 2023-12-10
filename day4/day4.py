import sys
sys.path.append('..\\utils')
from util import file_line_reader

class ScratchcardWinCalculator:
    '''
    Uses puzzle input path to find winning numbers on a scratch card.
    Calculates the points from these and sums them together.
    The puzzle assignment can be found in assignment4.md.
    '''
    def __init__(self, puzzle_input_path):
        self.puzzle_input_path = puzzle_input_path
        self.points_sum = 0

    def calculate_scratchcard_wins(self):
        for line_index, line in enumerate(file_line_reader(self.puzzle_input_path)):
            # Modify the string input into a list of winning numbers and a list of numbers that were found in the scratchcard
            _, numbers = line.split(':')
            winning_numbers_str, found_numbers_str = numbers.split('|')
            winning_numbers = winning_numbers_str.split(' ')
            found_numbers = found_numbers_str.split(' ')
            # Remove empty strings from data.
            winning_numbers = [number for number in winning_numbers if number.isdigit()]
            found_numbers = [number for number in found_numbers if number.isdigit()]
            # Collect the numbers that are found in both lists into a list
            matching_numbers = [number for number in found_numbers if number in winning_numbers]
            #print('matching_numbers', matching_numbers)
            if matching_numbers:
                # calculate points: points for the card = 2^(n-1), n being the number of matching numbers
                points = 2**(len(matching_numbers) - 1) 
                #print('points', points)
                self.points_sum += points
                #print('sum of points', self.points_sum)

        return self.points_sum

if __name__ == '__main__':
    engine_part_number_adder = ScratchcardWinCalculator('puzzle-input4.txt')
    points_sum = engine_part_number_adder.calculate_scratchcard_wins()
    print('win sum', points_sum)

