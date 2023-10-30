import requests

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-09-30&sortBy=publishedAt&apiKey=f01fddc8fb5c49eb8455549965f97e66"
api_key = "f01fddc8fb5c49eb8455549965f97e66"

request = requests.get(url)

response = request.text

print(response)