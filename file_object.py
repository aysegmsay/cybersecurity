import collections
import math
import binascii
import re
import os

signature_list = "Signature_list.csv"


class FileClass:
    def __init__(self, file_path):
        self.file_path = file_path
        self.context = self.read_file()
        self.entropy = self.calculate_entropy()
        self.signature = self.get_signature()

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

    def get_signature(self):
        with open(self.file_path, 'rb') as file:
            signature_file = file.read()
            hex_dump = str((binascii.hexlify(signature_file)).upper())[2:-1]
            with open(signature_list,'r') as s:
                signatures = s.read()
                s_list = re.split('\n|,', signatures)
                signature = s_list[::2]
                signature_type = s_list[1::2]

        for i in range(0,len(signature)):
            if hex_dump[:len(signature[i])] == signature[i]:
                return signature_type[i]
        return hex_dump

    def print_signature(self):
        print("Signature of the file:", self.get_signature())

    def get_file_size(self):
        return len(self.context)

    def print_file_size(self):
        print("File Size of the file:", self.get_file_size(), "bytes")

    def get_file_name(self):
        file_name = os.path.basename(self.file_path)
        return file_name

    def print_file_name(self):
        print("File Name:", self.get_file_name())
