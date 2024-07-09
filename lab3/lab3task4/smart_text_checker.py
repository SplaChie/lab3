from smart_text_reader import SmartTextReader

class SmartTextChecker(SmartTextReader):
    def read(self, file_path):
        print("Opening file...")
        data = super().read(file_path)
        print(f"File has {len(data)} lines and {sum(len(line) for line in data)} characters.")
        print("Closing file...")
        return data
