class ContainerFullException(Exception):
    pass


class ContainerEmptyException(Exception):
    pass


class Bucket():

    def __init__(self):
        self._contents = []

    def put(self, item):
        if(self.is_empty()):
            self._contents.append(item)
        else:
            raise ContainerFullException

    def get(self):
        try:
            return self._contents.pop(0)
        except Exception:
            raise ContainerEmptyException

    def is_empty(self):
        return len(self._contents) == 0

    def copy(self):
        nerwer = Bucket()
        nerwer._contents = self._contents
        return nerwer
