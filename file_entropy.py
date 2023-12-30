import collections
import math


def calculate_entropy(self):
    byte_frequency = collections.Counter(self.context)
    file_path = len(self.context)

    entropy = 0
    for byte_count in byte_frequency.values():
        probability = byte_count / file_path
        entropy -= probability * math.log2(probability)

    return entropy


def print_entropy(file_object):
    print("Entropy of the file:", calculate_entropy(file_object))



