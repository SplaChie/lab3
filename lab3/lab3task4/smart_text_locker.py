import re
from smart_text_reader import SmartTextReader

class SmartTextReaderLocker(SmartTextReader):
    def __init__(self, pattern):
        self.pattern = pattern

    def read(self, file_path):
        if re.match(self.pattern, file_path):
            print("Access denied!")
            return None
        else:
            return super().read(file_path)
