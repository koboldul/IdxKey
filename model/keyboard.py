from math import ceil
from math import inf

from collections import namedtuple

Key = namedtuple('Key', ['idx', 'cmd'])


class Keyboard(object):
    Up = 'u'
    Down = 'd'
    Left = 'l'
    Right = 'r'
    Press = 'p'

    def __init__(self, keys: list):
        self.keys = keys

    @classmethod
    def create_rectangular(cls, keys: list, keysPerRow: int):
        if len(keys) < keysPerRow:
            raise ValueError('No of keys < keys per row!')

        instance = cls(keys)

        instance.keyboardHeight = ceil(len(keys)/keysPerRow)
        instance.keyboardWidth = keysPerRow
        instance.keyboardGraph = [None] * len(keys)

        list(map(instance._add_nodes, range(0, len(keys))))
        return instance

    @classmethod
    def create_from_graph(cls, keys: list, graph: list):
        instance = cls(keys)
        instance.keyboardGraph = graph

        return instance

    @property
    def graph(self):
        return self.keyboardGraph.copy()

    """ Finds the shortest path between two keys.
        It accepts a factory function that will create
        the data structure used to explore the nodes.
        The factory has a function parameter used to calculate the score
        for a certin path.
    """
    def get_shortest_path(self, k1: str, k2: str, frontier_factory):
        idx1 = self.keys.index(k1)
        idx2 = self.keys.index(k2)

        if idx1 < 0 or idx2 < 0:
            raise ValueError('Non existent key!')

        frontier = frontier_factory(len)
        frontier.push([Key(idx1, Keyboard.Press)])
        best_so_far = inf
        visited = set()
        solutions = []

        while (frontier):
            current = frontier.pop()
            visited.add(current[-1])

            if any(self.keyboardGraph):
                for node in [n
                             for n in self.keyboardGraph[current[-1].idx]
                             if n not in visited]:
                    path = current.copy()
                    path.append(node)
                    if best_so_far > len(path):
                        if node.idx == idx2:
                            best_so_far = len(path)
                            solutions.append(path)
                        else:
                            if path not in frontier:
                                frontier.push(path)

        if any(solutions):
            return self._to_display(min(solutions, key=len))
        else:
            return []

    def _get_coord_from_idx(self, idx):
        return (int(idx/self.keyboardWidth), idx % self.keyboardWidth)

    def _to_display(self, solution: list):
        return [n.cmd for n in solution]

    def _add_nodes(self, index):
        self.keyboardGraph[index] = set()

        keybSize = len(self.keys)
        row, col = self._get_coord_from_idx(index)

        self._add_down_node(row, col, index, keybSize)
        self._add_up_node(row, col, index, keybSize)
        self._add_right_node(row, col, index, keybSize)
        self._add_left_node(row, col, index, keybSize)

    def _add_left_node(self, row, col, index, keybSize):
        nindex = (index-1) if (col-1) >= 0 else (row+1)*self.keyboardWidth-1
        if (nindex >= keybSize):
            nindex = keybSize-1
        if nindex != index:
            self.keyboardGraph[index].add(Key(idx=nindex, cmd=Keyboard.Left))

    def _add_down_node(self, row, col, index, keybSize):
        nindex = self.keyboardWidth*(row+1) + col
        if (row+1) >= self.keyboardHeight or nindex >= keybSize:
            nindex = col

        if nindex != index:
            self.keyboardGraph[index].add(Key(idx=nindex, cmd=Keyboard.Down))

    def _add_up_node(self, row, col, index, keybSize):
        nindex = (row-1)*self.keyboardWidth + col
        if (row-1) < 0:
            nindex = (self.keyboardHeight-1) * self.keyboardWidth + col
        if nindex >= keybSize:
            nindex = (self.keyboardHeight-2) * self.keyboardWidth + col
        if nindex != index:
            self.keyboardGraph[index].add(Key(nindex, Keyboard.Up))

    def _add_right_node(self, row, col, index, keybSize):
        nindex = index-self.keyboardWidth+1
        if (col+1) < self.keyboardWidth:
            nindex = index+1
        if (nindex >= keybSize):
            nindex = (self.keyboardHeight-1) * self.keyboardWidth
        if nindex != index:
            self.keyboardGraph[index].add(Key(nindex, Keyboard.Right))
