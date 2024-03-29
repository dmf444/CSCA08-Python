class ContainerFullException(Exception):
    pass


class ContainerEmptyException(Exception):
    pass


class Container():

    def __init__(self):
        self._contents = []

    def put(self, item):
        self._contents.insert(0, item)

    def get(self):
        try:
            return self._contents.pop(0)
        except Exception:
            raise ContainerEmptyException

    def is_empty(self):
        return len(self._contents) == 0
