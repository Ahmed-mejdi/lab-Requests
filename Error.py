import requests

# Example with an endpoint that returns a 404 error
response = requests.get("https://httpbin.org/status/404")
if response.status_code != 200:
    print(f"HTTP Error: {response.status_code}")