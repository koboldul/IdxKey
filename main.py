from model.data_cruncher import crunch
from model.keyboard import Key
from model.keyboard import Keyboard

import pprint
import sys
import json

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('''
            Please input the name of an existing file having this structure:

            [{
                "alphabet":["Q", "W", "E", "R", "T", "Y", "S"],
                "rowLength": 5,
                "startingFocus": "B",
                "word": "BAR"
             },
             {
                "alphabet":["R", "T", "Y", "A", "S", "D", "E", "U", "I", "O"],
                "rowLength": 3,
                "startingFocus": "Y",
                "word": "TILT"
            }]
        ''')
    else:
        file = sys.argv[1]
        print(f'Loading data from: {file}')

        data = []

        try:
            with open(file) as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f'The file {file} could not be found!')
        except json.decoder.JSONDecodeError:
            print(f'The file {file} does not contain valid json!')

        pp = pprint.PrettyPrinter(depth=6)
        crunch(data, lambda x: pp.pprint(x))
