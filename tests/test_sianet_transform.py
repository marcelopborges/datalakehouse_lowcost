from datetime import datetime
import pytest
from elt.transformer.sianet_transformer import Transformer
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

@pytest.fixture
def date():
    return datetime.strptime('02/01/2024', '%d/%m/%Y').strftime('%d/%m/%Y')


def test_convert_data_with_valid_input(example_data, date):
    transformer = Transformer("test_dna", example_data, date)
    result = transformer.convert_data()
    date_obj = datetime.strptime(date, "%d/%m/%Y")
    date_filename = date_obj.strftime("%d%m%Y")
    expected_file_path = os.path.join('../tmp', f'test_dna_{date_filename}.parquet')
    assert result == expected_file_path



@patch("os.path.exists")
@patch("os.makedirs")
@patch("pandas.DataFrame.to_parquet")
def test_save_as_parquet(mock_to_parquet, mock_makedirs, mock_path_exists, example_data, date):
    mock_path_exists.return_value = False
    transformer = Transformer("test_dna", example_data, date)
    transformer.convert_data()

    mock_makedirs.assert_called_once_with('../tmp')
    mock_to_parquet.assert_called()
