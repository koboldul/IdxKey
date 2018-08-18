import unittest
import ddt

from model.priority_queue import PriorityQueue
from model.keyboard import Keyboard
from tests.test_data_provider import DataProvider


@ddt.ddt
class KeyboardTests(unittest.TestCase):
    @ddt.data(*DataProvider.keyboard_cstr_data())
    def test_create_rectangular(self, case):
        # Arrange
        word, keysPerRow, graph = case
        # Act
        kb = Keyboard.create_rectangular(list(word), keysPerRow)
        # Assert
        list(map(lambda x: self.assertEqual(x[0], x[1]), zip(kb.graph, graph)))

    def test_create_rectangular_invalid(self):
        with self.assertRaises(ValueError) as cc:
            kb = Keyboard.create_rectangular(list('word'), 5)

    @ddt.data(*DataProvider.path_data())
    def test_shortest_path(self, case):
        # Arrange
        word, graph, k1, k2, result = case
        kb = Keyboard.create_from_graph(list(word), graph)
        # Act
        p = kb.get_shortest_path(k1, k2, lambda x: PriorityQueue(x))

        # Assert
        self.assertEqual(p, result)

if __name__ == '__main__':
    unittest.main()
