import requests

auth_token = "XXXXXXXX"

# Set the authorization header with bearer token
headers = {
    "Authorization": f"Bearer {auth_token}"
}

url = "https://httpbin.org/headers"
response = requests.get(url, headers=headers)
print(response.json())