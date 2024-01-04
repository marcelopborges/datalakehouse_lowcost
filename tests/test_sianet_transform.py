from datetime import datetime
import pytest
from elt.transformer import Transformer
from unittest.mock import patch
import os


@pytest.fixture
def example_data():
    return {
        "dados": [
            {"coluna1": 1, "coluna2": 2},
            {"coluna1": 3, "coluna2": 4}
        ]
    }


def test_convert_data_with_valid_input(example_data):
    transformer = Transformer("test_dna", example_data)
    result = transformer.convert_data()
    today = datetime.today().strftime('%Y%m%d')
    expected_file_path = os.path.join('tmp', f'test_dna_{today}.parquet')
    assert result == expected_file_path


@patch("os.path.exists")
@patch("os.makedirs")
@patch("pandas.DataFrame.to_parquet")
def test_save_as_parquet(mock_to_parquet, mock_makedirs, mock_path_exists, example_data):
    mock_path_exists.return_value = False

    transformer = Transformer("test_dna", example_data)
    transformer.convert_data()

    mock_makedirs.assert_called_once_with('tmp')
    mock_to_parquet.assert_called()
