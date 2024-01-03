import pandas as pd

from .base import Extractor


class CSVExtractor(Extractor):
    def __init__(self, file_path):
        self.file_path = file_path
        return

    def extract_km_rodado(self):
        data = pd.read_csv(self.file_path)
        return data
