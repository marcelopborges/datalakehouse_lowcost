from elt.Extractor import Extractor
from elt.loader import Loader
from elt.transformer import Transformer


class ELTProcess:
    def __init__(self):
        self.extractor = Extractor()
        self.loader = Loader()
        self.transformer = Transformer()
        return

    def execute_process(self):
        pass
