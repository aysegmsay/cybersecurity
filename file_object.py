import collections
import math
import binascii
import re
import hashlib
import os

signature_list = "Signature_list.csv"


class FileClass:
    def __init__(self, file_path):
        self.file_path = file_path
        self.context = self.read_file()
        self.entropy = self.calculate_entropy()
        self.signature = self.get_signature()
        self.file_sha1 = self.calc_file_hash_sha1()
        self.file_sha256 = self.calc_file_hash_sha256()
        self.file_md5 = self.calc_file_hash_md5()

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
    def calc_file_hash_sha1(self):
        file_sha1 = hashlib.new('sha1')
        with open(self.file_path, 'rb') as file:
            block = file.read(512)
            while block:
                file_sha1.update(block)
                block = file.read(512)
        return file_sha1.hexdigest()

    def print_file_sha1(self):
        print("SHA1:", self.calc_file_hash_sha1())

    def print_file_name(self):
        print("File Name:", self.get_file_name())
    def calc_file_hash_sha256(self):
        file_sha256 = hashlib.new('sha256')
        with open(self.file_path, 'rb') as file:
            block = file.read(512)
            while block:
                file_sha256.update(block)
                block = file.read(512)
        return file_sha256.hexdigest()

    def print_file_sha256(self):
        print("SHA256:", self.calc_file_hash_sha256())

    def calc_file_hash_md5(self):
        file_md5 = hashlib.new('md5')
        with open(self.file_path, 'rb') as file:
            block = file.read(512)
            while block:
                file_md5.update(block)
                block = file.read(512)
        return file_md5.hexdigest()

    def print_file_md5(self):
        print("MD5:", self.calc_file_hash_md5())
