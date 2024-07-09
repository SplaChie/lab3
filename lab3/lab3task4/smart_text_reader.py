class SmartTextReader:
    def read(self, file_path):
        with open(file_path, 'r') as file:
            return [list(line) for line in file.readlines()]
