import requests

# Make a GET Request

response = requests.get('https://api.github.com')
# print(response)

# if response.status_code == 200:
#     print("Success")
    
# elif response.status_code == 404:
#     print("Resource Not Found!")
    
# else:
#     print("Server Error!")

if response:
    print("Success!")
else:
    raise Exception(f"Non-success status code: {response.status_code}")