import requests


url1 = "https://wttr.in/%D0%A7%D0%B5%D1%80%D0%B5%D0%BF%D0%BE%D0%B2%D0%B5%D1%86?nMTq&lang=ru"
response = requests.get(url1)
response.raise_for_status()
print(response.text)


