import requests


url = "https://wttr.in/"
payload = {
    "svo": {"lang": "ru", "nMTq": ""},
    "London": {"lang": "ru", "nMTq": ""},
    "Череповец": {"lang": "ru", "nMTq": ""}
}
for place in payload:
    response = requests.get(f"{url}{place}", params=payload[place])
    response.raise_for_status()
    print(response.text)