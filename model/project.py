from sys import maxsize


class Project:

    def __init__(self, name, status=None, description=None):
        self.name = name
        self.description = description
        self.status = status

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def key_name(self):
        return self.name