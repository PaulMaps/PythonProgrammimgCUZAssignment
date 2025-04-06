from abc import ABC, abstractmethod

# Abstract Base Class
class FileHandler(ABC):
    
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

# Concrete class for text files
class TextFileHandler(FileHandler):
    
    def read(self):
        print("Reading from a text file...")

    def write(self, data):
        print(f"Writing text data: {data}")

# Concrete class for binary files
class BinaryFileHandler(FileHandler):
    
    def read(self):
        print("Reading from a binary file...")

    def write(self, data):
        print(f"Writing binary data: {data}")

# Example usage
text_handler = TextFileHandler()
text_handler.read()
text_handler.write("Hello, world!")

binary_handler = BinaryFileHandler()
binary_handler.read()
binary_handler.write(b"\x42\x69\x6e\x61\x72\x79")
