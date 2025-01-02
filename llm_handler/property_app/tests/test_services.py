import pytest
from unittest.mock import patch, Mock
import requests
from property_app.services.ollama_service import call_ollama

@patch('property_app.services.ollama_service.requests.post')
def test_call_ollama_success(mock_post):
    # Arrange
    prompt = "Hello, ollama! If you can read this message, please respond with 'Hello, human!'"
    model = "llama3.2:1b"
    expected_response = {"response": "Hello, human!"}
    
    mock_post.return_value = Mock(status_code=200)
    mock_post.return_value.json.return_value = expected_response

    # Act
    response = call_ollama(prompt, model)

    # Assert
    mock_post.assert_called_once_with(
        "http://ollama:11434/api/generate/",
        json={"model": model, "prompt": prompt, "stream": False},
        stream=False
    )
    assert response == expected_response["response"]

@patch('property_app.services.ollama_service.requests.post')
def test_call_ollama_failure(mock_post):
    # Arrange
    prompt = "Hello, world!"
    model = "llama3.2:1b"
    
    mock_post.return_value = Mock(status_code=500)
    mock_post.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError

    # Act & Assert
    with pytest.raises(requests.exceptions.HTTPError):
        call_ollama(prompt, model)