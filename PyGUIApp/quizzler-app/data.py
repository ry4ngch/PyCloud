import requests

parameters = {
    "difficulty": "medium",
    "amount": 10,
    "type": "boolean"
}

res = requests.get(url="https://opentdb.com/api.php", params=parameters)
res.raise_for_status()
question_data = res.json()['results']