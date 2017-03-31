class ContainerFullException(Exception):
    pass


class ContainerEmptyException(Exception):
    pass


class Steue():

    def __init__(self):
        self._contents = []
        self._on_right = True

    def put(self, item):
        self._contents.append(item)

    def get(self):
        try:
            if(self._on_right):
                returner = self._contents.pop(-1)
            else:
                returner = self._contents.pop(0)
            self._on_right = not self._on_right
            return returner
        except Exception:
            raise ContainerEmptyException

    def is_empty(self):
        return len(self._contents) == 0

    def peek(self):
        try:
            if(self._on_right):
                returner = self._contents[-1]
            else:
                returner = self._contents[0]
            self._on_right = not self._on_right
            return returner
        except Exception:
            raise ContainerEmptyException

    def copy(self):
        newer = Steue()
        newer._contents = self._contents[:]
        newer._on_right = self._on_right
        return newer