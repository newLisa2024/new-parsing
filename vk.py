import requests

img = "https://sun9-26.userapi.com/impg/M6hUdPDyrTgfSctKS63LbO_gi2LvzvqSNacKZA/Dtd2Od5tvLA.jpg?size=2560x1920&quality=95&sign=62dd2f6fc7227a6485e04781add4ee7e&type=album"

response = requests.get(img)

with open('img.png', 'wb') as file:
    file.write(response.content)