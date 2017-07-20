class GenericScanner(object):

    def __init__(self):
        self.data = ""

    def read_file(self, filename):
        with open(filename) as f:
            self.data = f.read()
