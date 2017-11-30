from FileProcessor.FileProcessor import FileProcessor


class CompareService:
    def __init__(self):
        self.current_files = []
        self.saved_files = []
        self.different_files = []

    def compare(self):
        file_processor = FileProcessor()
        self.current_files = file_processor.get_current_files()
        self.saved_files = file_processor.get_saved_files()





