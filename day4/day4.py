import sys
sys.path.append('..\\utils') # windows
try:
    from util import file_line_reader
except ModuleNotFoundError:
    sys.path.append('../utils') # linux
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
        self.scratchcards_sum = 0
        self.scratchcards = {1 : 1} # key = card number, value = number of copies

    def calculate_scratchcard_wins(self):
        #i = 0
        for line_index, line in enumerate(file_line_reader(self.puzzle_input_path)):
            current_card_number = line_index + 1
            print('current_card_number', current_card_number)
            print('self.scratchcards[current_card_number]', self.scratchcards[current_card_number])
            for i in range(self.scratchcards[current_card_number]):
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
                    for n in range(1, len(matching_numbers)):
                        self.scratchcards.setdefault(current_card_number + n, 0)
                        self.scratchcards[current_card_number + n] += 1
        for number_of_cards in self.scratchcards.values():
            self.scratchcards_sum += number_of_cards    

            #i += 1
            #if i >= 3:
            #    break
        print('self.scratchcards', self.scratchcards)
        return self.points_sum, self.scratchcards_sum 

if __name__ == '__main__':
    engine_part_number_adder = ScratchcardWinCalculator('puzzle-input4.txt')
    points_sum, scratchcards_sum = engine_part_number_adder.calculate_scratchcard_wins()
    print('win sum', points_sum)
    print('sum of scratchcards', scratchcards_sum)

