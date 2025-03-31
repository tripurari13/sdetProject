import requests
from unittest.mock import patch, Mock

BASE_URL = "https://jsonplaceholder.typicode.com"

# Mock response for requests.get
def mock_get(*args, **kwargs):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "title": "Test Product"}]
    return mock_response

def test_get_products():
    with patch("requests.get", side_effect=mock_get):
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200
        assert "title" in response.json()[0]  # Check if 'title' key exists in the response
