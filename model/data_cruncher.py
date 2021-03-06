from model.keyboard import Keyboard
from model.priority_queue import PriorityQueue
import multiprocessing as mp


def crunch(data: list, display_strategy=lambda x: print(x)):
    if not data:
        raise ValueError('No data to crunch!')

    pool = mp.Pool(processes=4)
    cases = [pool.apply(get_path_for_case, args=(c, idx))
             for idx, c
             in enumerate(data)]
    display_strategy(cases)


def get_path_for_case(case, case_no: int):

    if not is_case_valid(case):
        return

    try:
        row_length = int(case['rowLength'])
        kb = Keyboard.create_rectangular(
            keys=case['alphabet'],
            keysPerRow=row_length)

        def factory(func): return PriorityQueue(func)

        word = case['word']
        press_1 = True
        if word[0] != case['startingFocus']:
            word = f"{case['startingFocus']}{word}"
            press_1 = False
    except KeyError:
            print(f'The case does not contain valid information!')
            return
    except ValueError as e:
            print(f'Could not initialize the keyboard: {e}')
            return

    total_path = []
    for i in range(len(word)-1):
        start, end = word[i:i+2]
        p = kb.get_shortest_path(start, end, factory)
        if not press_1:
            press_1 = True
            p = p[1:]
        total_path.extend(p)

    total_path.append(Keyboard.Press)
    case['path'] = total_path
    case['distance'] = len([x for x in total_path if x != Keyboard.Press])

    return case


def is_case_valid(case):
    is_valid = True
    try:
        row_length = int(case['rowLength'])
    except ValueError:
            print(f'The rowLength must be a number!')
            is_valid = False
    except KeyError:
            print(f'The case does not contain rowLength information!')
            is_valid = False

    try:
        word = case['word']
        if not word:
            is_valid = False
    except KeyError:
            print(f'The case does not contain word information!')
            is_valid = False

    return is_valid
