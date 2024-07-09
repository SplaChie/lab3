from logger import Logger
from file_writer import FileWriter
from file_logger_adapter import FileLoggerAdapter

def main():
    logger = Logger()
    logger.log("This is a log message.")
    logger.error("This is an error message.")
    logger.warn("This is a warning message.")

    file_writer = FileWriter()
    file_logger = FileLoggerAdapter(file_writer)
    file_logger.log("This is a log message in the file.")
    file_logger.error("This is an error message in the file.")
    file_logger.warn("This is a warning message in the file.")

if __name__ == "__main__":
    main()