import requests
from requests.exceptions import HTTPError
# Make a GET Request

# response = requests.get('https://api.github.com')
# print(response)

# if response.status_code == 200:
#     print("Success")
    
# elif response.status_code == 404:
#     print("Resource Not Found!")
    
# else:
#     print("Server Error!")

# if response:
#     print("Success!")
# else:
#     raise Exception(f"Non-success status code: {response.status_code}")


# urls = ["https://api.github.com", "https://api.github.com/invalid"]

# for url in urls:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
    
#     except HTTPError as err:
#         print(f"HTTP Error Occurred: {err}")
        
#     except Exception as err:
#         print(f"Other Error Occurred: {err}")
        
#     else:
#         print("Success")

try:
    response = requests.get("https://api.github.com/search/repositories",params={"q": "language:python", "sort": "stars", "order": "desc"})
    json_response = response.json()
    popular_repos = json_response['items']
    
    for repo in popular_repos[:3]:
        print(f"Name: {repo['name']}")
        print(f"Description: {repo['description']}")
        print(f"Stars: {repo['stargazers_count']}\n")   
    response.raise_for_status()
    
except HTTPError as err:
    print(f"HTTP Error Occurred: {err}")
    
except Exception as err:
    print(f"Other Error Occurred: {err}")
    
else:
    print("Success!")
    