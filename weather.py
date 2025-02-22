import requests


if __name__ == '__main__':
    url = "https://wttr.in/"
    payload = {"lang": "ru", "nMTq": ""}
    locations = ["Череповец", "London", "svo"]
    for location in locations:
        response = requests.get(f"{url}{location}", params=payload)
        response.raise_for_status()
        print(response.text)