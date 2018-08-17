import bisect


class PriorityQueue(object):
    def __init__(self, utility_func=lambda x: x):
        self.storage = []
        self.utility_func = utility_func

    def push(self, val):
        bisect.insort(self.storage, (self.utility_func(val), val))

    def pop(self):
        return self.storage.pop(0)[1]

    def __len__(self):
        return len(self.storage)

    def __contains__(self, val):
        any(val == pair[1] for pair in self.storage)

    def __getitem__(self, key):
        for _, item in self.storage:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (_, item) in enumerate(self.storage):
            if item == key:
                self.storage.pop(i)
