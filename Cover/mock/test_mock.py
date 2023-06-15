from unittest.mock import patch, MagicMock
from example_mock import get_only_numbers, API


def test_read_only_numbers():
    test_data = ["1,4,5,25,aa,bb,23,4", "324,24,234www,1,23", "545,3w,32"]
    expected = "1|4|5|25|23|4|324|24|1|23|545|32"
    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data #  get_data method mocking
    #use fake api
    with patch('example_mock.API', fake_api):
        # patch replaces the original object and context manager defines the scope of use of the mock
        result = get_only_numbers()
        assert result == expected
