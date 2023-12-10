import sys
sys.path.append('..\\utils')
from util import file_line_reader


class CubeGameCounter:
    '''
    Sums together the game IDs of the games that meet the criteria from the given puzzle input filepath.
    The max count of red, blue and green cubes are given at input, and these are used to determine whether a game meets
    the criteria. If one game (one line of puzzle input) contains more than the max number of some color cubes (red, green or blue), 
    then the game does not meet the criteria.
    More information in file assignment2.md.
    '''
    def __init__(self, puzzle_input_path, max_red, max_blue, max_green):
        self.max_colors_dict = {'red': max_red, 'blue': max_blue, 'green': max_green}
        self.max_red = max_red
        self.max_blue = max_blue
        self.max_green = max_green
        self.puzzle_input_path = puzzle_input_path
        self.game_id_sum = 0
        self.cubes_power_sum = 0

    def count_cube_games(self):
        # process one line at a time, which represents one game
        for line in file_line_reader(self.puzzle_input_path):
            # first extract the game ID
            game_id_string, cube_input = line.split(':')
            game_id = int(game_id_string.replace('Game ', ''))

            # make a flat list of all the cube colors with the number in one game
            cube_input = cube_input.replace(';', ',').split(',')
            most_colors_dict = {'red': 0, 'blue': 0, 'green': 0}

            # find the largest number of each color cubes in the game and save it in the dict
            for cubes in cube_input:
                number, color = cubes.strip().split(' ')
                if int(number) > most_colors_dict[color]:
                    most_colors_dict[color] = int(number)

            # compare the values in the most_colors_dict to the max color values that were given at init
            # to see if game has too many cubes of some color
            game_meets_criteria = True
            for key, value in most_colors_dict.items():
                if value > self.max_colors_dict[key]:
                    game_meets_criteria = False

            # if game has less than or as many of each color cubes than the max numbers given at input, 
            # we can add the game id to the total sum
            if game_meets_criteria: 
                self.game_id_sum += game_id
            
            # calculate the power of a set of cubes for each game and sum them for part 2
            cubes_power = most_colors_dict['red'] * most_colors_dict['blue'] * most_colors_dict['green']
            self.cubes_power_sum += cubes_power

        return (self.game_id_sum, self.cubes_power_sum)

if __name__ == '__main__':
    cube_game_counter = CubeGameCounter('puzzle-input2.txt', max_red=12, max_blue=14, max_green=13)
    game_id_sum, cubes_power_sum = cube_game_counter.count_cube_games()
    print('game_id_sum', game_id_sum)
    print('cubes_power_sum', cubes_power_sum)