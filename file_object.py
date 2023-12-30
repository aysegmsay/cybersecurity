from file_entropy import calculate_entropy


class FileClass:
    def __init__(self, file_path):
        self.file_path = file_path
        self.context = self.read_file()
        self.entropy = calculate_entropy(self)

    def read_file(self):  # burda dosya okunuyor<3
        with open(self.file_path, 'rb') as file:
            return file.read()
