import requests

url = "https://www.example.com"
response = requests.get(url)
print(response)  # Prints the response object with status code
print(response.status_code)