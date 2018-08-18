import unittest
import ddt

from unittest.mock import MagicMock

from model.keyboard import Keyboard
from model.data_cruncher import get_path_for_case
from tests.test_data_provider import DataProvider


@ddt.ddt
class DataCruncherTests(unittest.TestCase):
    @ddt.data(*DataProvider.full_path_data())
    def test_create_rectangular(self, case):
        # Arrange
        data, paths, expected = case
        expected_path, expected_distance = expected

        kb = Keyboard([])
        Keyboard.create_rectangular = MagicMock(return_value=kb)

        kb.get_shortest_path = MagicMock(side_effect=paths)

        # Act
        result = get_path_for_case(data, 1)

        # Assert
        kb.get_shortest_path.assert_called()
        self.assertEqual(result['distance'], expected_distance)
        self.assertEqual(result['path'], expected_path)

if __name__ == '__main__':
    unittest.main()
