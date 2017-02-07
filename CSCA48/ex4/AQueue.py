class ContainerFullException(Exception):
    pass


class ContainerEmptyException(Exception):
    pass


class AQueue():

    def __init__(self):
        self._contents = []
        self._on_left = True

    def put(self, item):
        if(self._on_left):
            self._contents.insert(0, item)
        else:
            self._contents.append(item)
        self._on_left = not self._on_left

    def get(self):
        try:
            if (self._on_left):
                returner = self._contents.pop(0)
            else:
                returner = self._contents.pop(-1)
            self._on_left = not self._on_left
            return returner
        except Exception:
            raise ContainerEmptyException

    def is_empty(self):
        return (len(self._contents) == 0)
