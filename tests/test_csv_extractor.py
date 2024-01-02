import sys
from pathlib import Path
import os
import pandas as pd
from unittest.mock import Mock, patch

root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))
from elt.extractor.csv_extractor import CSVExtractor


def test_extractor_from_csv():
    df_example = pd.DataFrame({
        'coluna1': [1, 2, 3],
        'coluna2': ['a', 'b', 'c']
    })
    file_path = 'caminho/ficticio/test.csv'
    with patch('pandas.read_csv', return_value=df_example) as mock_read_csv:
        extractor = CSVExtractor(file_path)
        result = extractor.extract_km_rodado()
        mock_read_csv.assert_called_once_with(file_path)

    assert isinstance(result, pd.DataFrame)
    assert not result.empty