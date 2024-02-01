import os
import pytest
import pandas as pd
from mtbl_savekit import exporter as sk


class TestExporter:
    df = None
    full_path = ""

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
        yield
        os.remove(self.full_path)

    def test_export_dataframe_to_csv(self):
        sk.export_dataframe(self.df, "test", ".csv", "./temp")
        self.full_path = "./temp/test.csv"
        assert os.path.exists(self.full_path)

    def test_export_dataframe_to_json(self):
        sk.export_dataframe(self.df, "test", ".json", "./temp")
        self.full_path = "./temp/test.json"
        assert os.path.exists(self.full_path)

    def test_export_dataframe_to_json_without_schema(self):
        sk.export_dataframe(self.df, "test", ".json", "./temp", schema=False)
        self.full_path = "./temp/test.json"
        assert os.path.exists(self.full_path)

    def test_export_dataframe_without_proper_file_type(self):
        sk.export_dataframe(self.df, "test", "json", "./temp")
        self.full_path = "./temp/test.json"
        assert os.path.exists(self.full_path)

