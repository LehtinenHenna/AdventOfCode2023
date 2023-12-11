import sys
sys.path.append('..\\utils') # windows
try:
    from util import file_line_reader, file_reader
except ModuleNotFoundError:
    sys.path.append('../utils') # linux
    from util import file_line_reader, file_reader

class ScratchcardWinCalculator:
    '''
    Uses puzzle input path to solve part 1 and part 2 puzzles. 
    The puzzle assignment can be found in assignment4.md.
    '''
    def __init__(self, puzzle_input_path):
        self.puzzle_input_path = puzzle_input_path
        self.points_sum = 0
        self.scratchcards_sum = 0
        self.scratchcards = {} # key = card number, value = number of copies

    def find_matching_numbers(self, line):
        '''
        Gets a line of the puzzle input with  winning numbers and 
        numbers that were found in the current scratchcard.
        Cleans the data and returns a list of numbers that 
        were a match between the winning and found numbers.
        '''
        # Modify the string input into a list of winning numbers 
        # and a list of numbers that were found in the scratchcard
        _, numbers = line.split(':')
        winning_numbers_str, found_numbers_str = numbers.split('|')
        winning_numbers = winning_numbers_str.split(' ')
        found_numbers = found_numbers_str.split(' ')
        # Remove empty strings from data.
        winning_numbers = [number for number in winning_numbers if number.isdigit()]
        found_numbers = [number for number in found_numbers if number.isdigit()]
        # Collect the numbers that are found in both lists into a list
        matching_numbers = [number for number in found_numbers if number in winning_numbers]
        return matching_numbers

    def calculate_scratchcard_wins_part1(self):
        '''Solves part 1 puzzle.'''
        for line_index, line in enumerate(file_line_reader(self.puzzle_input_path)):
            matching_numbers = self.find_matching_numbers(line)
            if matching_numbers:
                # calculate points: points for the card = 2^(n-1), n being the number of matching numbers
                points = 2**(len(matching_numbers) - 1) 
                self.points_sum += points
        return self.points_sum
    
    def calculate_scratchcard_wins_part2(self):
        ''' Solves part 2 puzzle.'''
        file_content = file_reader(self.puzzle_input_path).splitlines()
        card_numbers_range = len(file_content)
        # process each card number
        for line_index, line in enumerate(file_content):
            current_card_number = line_index + 1
            self.scratchcards.setdefault(current_card_number, 0)
            self.scratchcards[current_card_number] += 1
            matching_numbers = self.find_matching_numbers(line)
            if matching_numbers:
                # process copies of the card
                for i in range(self.scratchcards[current_card_number]):
                    if len(matching_numbers) + current_card_number > card_numbers_range:
                        matching_numbers = matching_numbers[:card_numbers_range + 1 - current_card_number]
                    for n in range(1, len(matching_numbers) + 1):
                        self.scratchcards.setdefault(current_card_number + n, 0)
                        self.scratchcards[current_card_number + n] += 1
        for number_of_cards in self.scratchcards.values():
            self.scratchcards_sum += number_of_cards
        print(self.scratchcards)
        return self.scratchcards_sum


if __name__ == '__main__':
    engine_part_number_adder = ScratchcardWinCalculator('puzzle-input4.txt')
    points_sum = engine_part_number_adder.calculate_scratchcard_wins_part1()
    scratchcards_sum = engine_part_number_adder.calculate_scratchcard_wins_part2()
    print('win sum', points_sum)
    print('sum of scratchcards', scratchcards_sum)

