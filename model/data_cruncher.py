from model.keyboard import Keyboard
from model.priority_queue import PriorityQueue
import multiprocessing as mp


def crunch(data: list, display_strategy=lambda x: print(x)):
    if not data:
        raise Exception('No data to crunch!')

    pool = mp.Pool(processes=4)
    cases = [pool.apply(get_path_for_case, args=(c, idx))
             for idx, c
             in enumerate(data)]
    cases = list([get_path_for_case(c, idx) for idx, c in enumerate(data)])
    display_strategy(cases)


def get_path_for_case(case, case_no: int):
    try:
        kb = Keyboard.create_rectangular(
            keys=case['alphabet'],
            keysPerRow=int(case['rowLength']))

        def factory(func): return PriorityQueue(func)

        word = case['word']
        press_1 = True
        if word[0] != case['startingFocus']:
            word = f"{case['startingFocus']}{word}"
            press_1 = False
    except KeyError:
            print(f'The case does not contain valid information!')
            return
    except ValueError:
            print(f'The rowLength must be a number!')
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
