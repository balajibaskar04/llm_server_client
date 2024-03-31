import requests

response=requests.post(
    "http://localhost:8000/essay/invoke",
    json={'input':{'topic':"help to clear python interview"}})

print(response.json()['output']['content'])