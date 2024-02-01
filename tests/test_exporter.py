import os
import pytest
import pandas as pd
from mtbl_savekit import exporter as sk


class TestExporter:
    df = None

    @pytest.fixture(autouse=True)
    def setup(self):
        self.df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

    def test_export_dataframe_to_csv(self):
        sk.export_dataframe(self.df, "test", ".json", directory="./temp")
        full_path = "./temp/test.json"
        assert os.path.exists(full_path)
        os.remove(full_path)

    def test_export_dataframe_to_json(self):
        sk.export_dataframe(self.df, "test", ".csv", directory="./temp")
        full_path = "./temp/test.csv"
        assert os.path.exists(full_path)
        os.remove(full_path)

