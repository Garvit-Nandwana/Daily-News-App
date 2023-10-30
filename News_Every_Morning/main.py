import requests
from emails import send_emails

# For adding the topic that the user needs
topic = 'Tesla'

url = """https://newsapi.org/v2/everything?q={topic}&
from=2023-09-30&sortBy=publishedAt&apiKey=f01fddc8fb5c49eb8455549965f97e66&language=en"""

api_key = "f01fddc8fb5c49eb8455549965f97e66"

# Make Request
request = requests.get(url)

# Get a dictionary with the required data
response = request.json()

# Accessing the article title and description
body = ""
# Limiting the articles to a maximum of 20
for article in response['articles'][:20]:
    body = body + article['title'] \
          + '\n' + article['description'] \
          + '\n' + article['url'] + 2 * '\n' 

body = body.encode('utf8')
send_email = send_emails(body)