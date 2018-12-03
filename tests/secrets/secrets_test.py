from git_secrets.secrets import secrets
from unittest.mock import patch, mock_open


@patch('builtins.open', new_callable=mock_open, read_data='DogCow\nMoof\n')
def test_load_patterns(open_mock):
    secret_regexes = secrets.load_patterns()

    assert len(secret_regexes) == 4
