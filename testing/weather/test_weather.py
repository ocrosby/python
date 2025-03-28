import pytest

from .weather import fetch_weather_data

@pytest.fixture
def mock_response_200(mocker):
    response = mocker.Mock()
    response.status_code = 200
    response.json.return_value = {"temperature": "20C", "condition": "Sunny"}
    return response

@pytest.fixture
def mock_response_404(mocker):
    response = mocker.Mock()
    response.status_code = 404
    return response

@pytest.fixture
def mock_response_500(mocker):
    response = mocker.Mock()
    response.status_code = 500
    return response

@pytest.fixture
def mock_api_client(mocker):
    def _mock_api_client(response):
        client = mocker.Mock()
        client.get.return_value = response
        return client
    return _mock_api_client

@pytest.mark.parametrize(
    "response_fixture, expected_result",
    [
        ("mock_response_200", {"temperature": "20C", "condition": "Sunny"}),
        ("mock_response_404", None),
        ("mock_response_500", None),
    ],
    ids=[
        "200 OK Response",
        "404 Not Found Response",
        "500 Internal Server Error Response",
    ]
)
def test_fetch_weather_data(request, mock_api_client, response_fixture, expected_result):
    response = request.getfixturevalue(response_fixture)
    client = mock_api_client(response)

    # Act
    result = fetch_weather_data(client)

    # Assert
    assert result == expected_result
    client.get.assert_called_once_with("https://api.weather.com/data")
