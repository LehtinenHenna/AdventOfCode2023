import sys
sys.path.append('..\\utils') # windows
try:
    from util import file_line_reader, file_reader
except ModuleNotFoundError:
    sys.path.append('../utils') # linux
    from util import file_line_reader, file_reader


class SeedLocationMapper:

    def __init__(self, puzzle_input_path):
        self.puzzle_input_path = puzzle_input_path
        self.seeds = []
        self.seed_to_soil_map = {} # key = seed number, value = soil number
        self.soil_to_fertilizer_map = {} # key = soil number, value = fertilizer number
        self.fertilizer_to_water_map = {} # key = fertilizer number, value = water number
        self.water_to_light_map = {} # key = water, value = light
        self.light_to_temperature_map = {} # key = light, value = temperature
        self.temperature_to_humidity_map = {} # key = temperature, value = humidity
        self.humidity_to_location_map = {} # key = humidity, value = location
    
    def seed_to_location_mapper(self):
        pass

    def create_maps(self):
        pass