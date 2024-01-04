import collections
import math


class FileClass:
    def __init__(self, file_path):
        self.file_path = file_path
        self.context = self.read_file()
        self.entropy = self.calculate_entropy()

    def read_file(self):  # burda dosya okunuyor<3
        with open(self.file_path, 'rb') as file:
            return file.read()

    def calculate_entropy(self):
        byte_frequency = collections.Counter(self.context)
        file_path = len(self.context)

        entropy = 0
        for byte_count in byte_frequency.values():
            probability = byte_count / file_path
            entropy -= probability * math.log2(probability)

        return entropy

    def print_entropy(self):
        print("Entropy of the file:", self.calculate_entropy())

