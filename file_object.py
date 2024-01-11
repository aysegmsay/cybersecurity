import collections
import math
import binascii
import re
import hashlib
import os
import requests

signature_list = "Signature_list.csv"


class FileClass:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = self.get_file_name()
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

    def is_encrypted(self, entropy_threshold=5.0):
        encrypted=True
        non_encrypted=False
        if self.calculate_entropy() > entropy_threshold:

            return True# Şifrelenmiş
        else:
            return False  # Şifrelenmemiş

    def print_entropy(self):
        print("Entropy of the file:", self.calculate_entropy())

    def get_signature(self):
        with open(self.file_path, 'rb') as file:
            signature_file = file.read()
            hex_dump = str((binascii.hexlify(signature_file)).upper())[2:-1]
            with open(signature_list, 'r') as s:
                signatures = s.read()
                s_list = re.split('\n|,', signatures)
                signature = s_list[::2]
                signature_type = s_list[1::2]

        for i in range(0, len(signature)):
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
        file_name_with_extension = os.path.basename(self.file_path)
        file_name_without_extension, _ = os.path.splitext(file_name_with_extension)
        return file_name_without_extension

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

    def get_file_strings(self):
        return self.context

    def print_file_strings(self):
        print("File Strings of the file:", self.get_file_strings())

    def search_from_virus_total(self):
        url = f"https://www.virustotal.com/api/v3/files/{self.file_md5}"
        headers = {
            "accept": "application/json",
            "x-apikey": "0236ab3404b787b7ab0493ddf171b4ef8fe1196aebc3ac3c71d0cc7caf560dc6"
        }
        response = requests.get(url, headers=headers)
        return response



    def analyze_file(self):
        result_text = (
            f"File Name: {self.get_file_name()}\n"
            f"File Size: {self.get_file_size()} bytes\n"
            f"Entropy: {self.calculate_entropy()}\n"
            f"Signature: {self.get_signature()}\n"
            f"SHA1: {self.calc_file_hash_sha1()}\n"
            f"SHA256: {self.calc_file_hash_sha256()}\n"
            f"MD5: {self.calc_file_hash_md5()}\n"
            f"file string: {self.get_file_strings()[:10]}\n"
            f"virustotal result : {self.search_from_virus_total()}\n"
            f"encrypted possibility:{self.is_encrypted()}"

        )
        return result_text
