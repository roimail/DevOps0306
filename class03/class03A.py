import requests
response = requests.get("https://api.github.com/users/avielb/repos")
if response.status_code == 200:
    print("github is up")
#print(response.text)

'''
repos = response.json()
for repo in repos:
    if "devops" in str(repo["name"]).lower():
        print(repo["name"])
'''