import pda.get_weather_api as my_module
from unittest.mock import patch


@patch('pda.get_weather_api.requests.get')
def test_get_data_from_weather_api(mock_get):
    # mocked JSON
    mock_get.return_value.json.return_value = {
        'properties': {'forecastHourly': 'https://api.weather.gov/gridpoints/LSX/27,123/forecast/hourly'}
    }
    actual_output = my_module.get_weather(39.7456, -92.0892)
    excepted_output = 'https://api.weather.gov/gridpoints/LSX/27,123/forecast/hourly'
    assert actual_output == excepted_output, f"Expected:{excepted_output} differs from actual value {actual_output}"
