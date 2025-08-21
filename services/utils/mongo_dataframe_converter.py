import pandas as pd

class ConvertToDF:
    @staticmethod
    def convert(mongofile):
        df = pd.DataFrame(mongofile)
        return df