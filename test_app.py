from app import app  # Import your Flask app

def test_hello_world():
    client = app.test_client()  # Fake browser
    response = client.get('/')   # Visit the home page

    assert response.status_code == 200          # Should load successfully
    assert b"Hello, World!" in response.data    # Should contain the text