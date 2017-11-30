import sys,os
import datetime
import json


class File:
    def __init__(self):
        self.path = ""
        self.filename = ""
        self.timestamp = datetime()

    def __init__(self, path, filename, timestamp):
        self.path = path
        self.filename = filename
        self.timestamp = timestamp


class FileProcessor:
    current_files = []
    saved_files = []

    def read_сurrent_files(self):
        for dirpath, dirnames, filenames in os.walk("C:\\tmp"):
            for filename in [f for f in filenames if f.endswith(".txt")]:
                file = File(dirpath, filename,
                            datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(dirpath, filename))))
                self.current_files += [file]

    def read_saved_files(self):
        f = open("data.txt", "r")
        saved_files_array = json.loads(f.read())
        for saved_file in saved_files_array:
            file = File(saved_file[0], saved_file[1], saved_file[2])
            self.saved_files += [file]

    def save_current_files(self):
        #rewrite file
        f = open("data.txt", 'w+')
        files_array = []
        for file in self.current_files:
            files_array += [[file.path, file.filename, str(file.timestamp)]]

        f.write(json.dumps(files_array))
        f.close()

    def get_saved_files(self):
        self.read_saved_files()
        return self.saved_files

    def get_current_files(self):
        self.read_сurrent_files()
        return self.current_files


