# RestAPI
Generic RestAPI 

How It Works
GET /posts: Fetches a list of posts and validates the response is a list with a 200 status code.
POST /posts: Creates a new post and validates that the response matches the input payload and returns a 201 status code.
PUT /posts/1: Updates a specific post and verifies that the updated data matches the request payload.
DELETE /posts/1: Deletes a post and confirms the status code is 200.

How to Run the Script
Save the script as mock_api_tester.py.
Ensure you have Python installed and the requests library (pip install requests).

Run the script:
python mock_api_tester.py
