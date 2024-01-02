import pandas as pd


class Loader(object):
    def __init__(self):
        return

    def load_to_dataframe(self, raw_data):
        dataframe = pd.DataFrame([raw_data])
        return dataframe