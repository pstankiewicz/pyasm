class GenericScanner(object):

    def __init__(self):
        self.data = ""
        self.parsed_data = []
        self.line_index = 1
        self.column_index = 1
        self.data_index = 0

    def read_file(self, filename):
        with open(filename) as f:
            self.data = f.read()
        self.parse_input(self.data)

    def parse_input(self, data):
        for ch in data:
            ch = self.normalize(ch)
            self.parsed_data.append(
                [self.line_index, self.column_index, ch],
            )
            if ch != "NEWLINE":
                self.column_index += 1
            else:
                self.line_index += 1
                self.column_index = 1

        self.parsed_data.append(
            [self.line_index, self.column_index, 'EOF'],
        )

    def normalize(self, char):
        NORMALS = {
            ' ': 'SPACE',
            '\n': 'NEWLINE',
            '\t': 'TAB',
        }
        return NORMALS.get(char, char)
