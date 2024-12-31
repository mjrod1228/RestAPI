import requests

# Mock API URL (Replace with actual mock API URL)
BASE_URL = "https://jsonplaceholder.typicode.com"

# Function to validate a GET request
def test_get_posts():
    print("Testing GET /posts...")
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200, "GET /posts failed!"
    data = response.json()
    assert isinstance(data, list), "Expected a list of posts!"
    print(f"GET /posts passed! Retrieved {len(data)} posts.")

# Function to validate a POST request
def test_create_post():
    print("Testing POST /posts...")
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201, "POST /posts failed!"
    data = response.json()
    assert data["title"] == payload["title"], "Title mismatch!"
    assert data["body"] == payload["body"], "Body mismatch!"
    assert data["userId"] == payload["userId"], "UserID mismatch!"
    print("POST /posts passed!")

# Function to validate a PUT request
def test_update_post():
    print("Testing PUT /posts/1...")
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200, "PUT /posts/1 failed!"
    data = response.json()
    assert data["title"] == payload["title"], "Title mismatch after update!"
    assert data["body"] == payload["body"], "Body mismatch after update!"
    print("PUT /posts/1 passed!")

# Function to validate a DELETE request
def test_delete_post():
    print("Testing DELETE /posts/1...")
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, "DELETE /posts/1 failed!"
    print("DELETE /posts/1 passed!")

# Run tests
if __name__ == "__main__":
    try:
        test_get_posts()
        test_create_post()
        test_update_post()
        test_delete_post()
        print("\nAll tests passed!")
    except AssertionError as error:
        print(f"Test failed: {error}")
