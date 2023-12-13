import sys
sys.path.append('..\\utils') # windows
try:
    from util import file_line_reader, file_reader
except ModuleNotFoundError:
    sys.path.append('../utils') # linux
    from util import file_line_reader, file_reader


class SeedLocationMapper:
    '''
    Uses a given filepath to collect data and find the smallest 
    location number that corresponds to any of the initial seed numbers.
    More information in assignment5.md.
    '''

    def __init__(self, puzzle_input_path):
        self.puzzle_input_path = puzzle_input_path
        self.seeds = [] # Seed numbers

        # Each of the map lists contain embedded lists.
        # Each embedded list contains destination range start number, 
        # source range number and range length number in that order.
        self.seed_to_soil_map = []
        self.soil_to_fertilizer_map = []
        self.fertilizer_to_water_map = []
        self.water_to_light_map = []
        self.light_to_temperature_map = []
        self.temperature_to_humidity_map = []
        self.humidity_to_location_map = []

        # Used for organizing data in the right lists
        self.map_identifiers = {
            'seed-to-soil': False,
            'soil-to-fertilizer': False,
            'fertilizer-to-water': False,
            'water-to-light': False,
            'light-to-temperature': False,
            'temperature-to-humidity': False,
            'humidity-to-location': False
        }
    
    def main(self):
        '''
        Use internal methods and given filepath to find the smallest location number that 
        corresponds to any of the initial seed numbers.
        '''
        self.create_maps()
        locations = []
        for seed in self.seeds:
            location = self.seed_to_location_mapper(seed)
            locations.append(location)
        return min(locations)
    
    def seed_to_location_mapper(self, seed_number):
        '''Find location number for a seed number.'''
        soil_number = self.convert_number(seed_number, self.seed_to_soil_map)
        fertilizer_number = self.convert_number(soil_number, self.soil_to_fertilizer_map)
        water_number = self.convert_number(fertilizer_number, self.fertilizer_to_water_map)
        light_number = self.convert_number(water_number, self.water_to_light_map)
        temperature_number = self.convert_number(light_number, self.light_to_temperature_map)
        humidity_number = self.convert_number(temperature_number, self.temperature_to_humidity_map)
        location_number = self.convert_number(humidity_number, self.humidity_to_location_map)
        return location_number
    
    def convert_number(self, source_number, map_list):
        '''Convert given source number into a destination number according to a map list.'''
        for lst in map_list:
            destination_range_start = lst[0]
            source_range_start = lst[1]
            range_length = lst[2]
            if  source_range_start <= source_number < (source_range_start + range_length):
                # e.g., with map list [2, 44, 5] and source number 45, the destination number is 3
                destination_number = source_number - source_range_start + destination_range_start
                return destination_number
        # no match was found, so the destination number and source number are the same
        return source_number

    def create_maps(self):
        '''Collect data from the given filepath into lists.'''
        for index, line in enumerate(file_line_reader(self.puzzle_input_path)):
            # create seeds list
            if line.startswith('seeds:'):
                line = line.replace('seeds:', '')
                self.seeds = line.split(' ')
                self.seeds = [int(seed) for seed in self.seeds if seed.isdigit()]
            else:
                if len(line) > 0:
                    if not line[0].isdigit():
                        # the following lines of the file contain numbers for a new map
                        for key, value in self.map_identifiers.items():
                            if line.startswith(key):
                                for indentifier in self.map_identifiers:
                                    # Activate the current line identifier and deactivate all the others 
                                    # to collect the numbers in the following lines of the file in the right map list
                                    if key == indentifier:
                                        self.map_identifiers[indentifier] = True
                                    else:
                                        self.map_identifiers[indentifier] = False
                    else:
                        # collect numbers in the activated list
                        for key, value in self.map_identifiers.items():
                            if value == True:
                                # select the activated list
                                map_list = getattr(self, key.replace('-', '_') + '_map')
                        dest_source_range_list = line.split(' ')
                        dest_source_range_list = [int(number_str) for number_str in dest_source_range_list]
                        map_list.append(dest_source_range_list)
                

if __name__ == '__main__':
    seed_location_mapper = SeedLocationMapper('puzzle-input5.txt')
    smallest_location = seed_location_mapper.main()
    print('Min location', smallest_location)