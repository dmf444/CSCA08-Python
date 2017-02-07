class ContainerFullException(Exception):
    pass


class ContainerEmptyException(Exception):
    pass


class NQueue():

    def __init__(self):
        self._contents = []

    def put(self, item):
        self._contents.append(item)

    def get(self):
        try:
            if(len(self._contents) > 1):
                return self._contents.pop(1)
            else:
                return self._contents.pop(0)
        except Exception:
            raise ContainerEmptyException

    def is_empty(self):
        return len(self._contents) == 0
