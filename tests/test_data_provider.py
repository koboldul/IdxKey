from model.keyboard import Key
from model.keyboard import Keyboard


class DataProvider(object):
    @staticmethod
    def keyboard_cstr_data():
        def create_keys(u: int=None, r: int=None, d: int=None, l: int=None):
            key = set()
            if u is not None:
                key.add(Key(u, Keyboard.Up))
            if r is not None:
                key.add(Key(r, Keyboard.Right))
            if d is not None:
                key.add(Key(d, Keyboard.Down))
            if l is not None:
                key.add(Key(l, Keyboard.Left))

            return key

        g1 = [
            create_keys(10, 1, 5, 4), create_keys(11, 2, 6, 0),
            create_keys(7, 3, 7, 1), create_keys(8, 4, 8, 2),
            create_keys(9, 0, 9, 3), create_keys(0, 6, 10, 9),
            create_keys(1, 7, 11, 5), create_keys(2, 8, 2, 6),
            create_keys(3, 9, 3, 7), create_keys(4, 5, 4, 8),
            create_keys(5, 11, 0, 11), create_keys(6, 10, 1, 10)]
        g2 = [create_keys(r=1, l=2),
              create_keys(r=2, l=0),
              create_keys(r=0, l=1)]
        g3 = [create_keys(2, 1, 2, 1),
              create_keys(r=0, l=0),
              create_keys(u=0, d=0)]
        g4 = []

        return [('qwerastyuiot', 5, g1),
                ('qwe', 3, g2),
                ('qed', 2, g3),
                ('q', 1, g4)]

    @classmethod
    def path_data(cls):
        test_cases = []

        d = cls.keyboard_cstr_data()
        test_cases.append((d[0][0], d[0][2], 'w', 'o', ['p', 'l', 'u']))
        test_cases.append((d[0][0], d[0][2], 'u', 'o', ['p', 'r', 'r', 'd']))
        test_cases.append((d[3][0], d[3][2], 'q', 'q', []))

        return test_cases
