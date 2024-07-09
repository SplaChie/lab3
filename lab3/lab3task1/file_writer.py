class FileWriter:
    def write(self, message):
        with open('log.txt', 'a') as f:
            f.write(message)

    def write_line(self, message):
        with open('log.txt', 'a') as f:
            f.write(message + '\n')
