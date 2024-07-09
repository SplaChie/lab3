from smart_text_reader import SmartTextReader
from smart_text_checker import SmartTextChecker
from smart_text_locker import SmartTextReaderLocker

def main():
    reader = SmartTextReader()
    checker = SmartTextChecker()
    locker = SmartTextReaderLocker(r'.*restricted.*')

    # Example usage:
    file_path = "example.txt"

    print("SmartTextReader:")
    data = reader.read(file_path)
    print(data)

    print("\nSmartTextChecker:")
    data = checker.read(file_path)
    print(data)

    print("\nSmartTextReaderLocker:")
    data = locker.read(file_path)
    print(data)

if __name__ == "__main__":
    main()
