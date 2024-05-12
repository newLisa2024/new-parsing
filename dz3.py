import requests


def create_post(title, body, user_id):
    # URL API для отправки POST-запроса
    url = "https://jsonplaceholder.typicode.com/posts"

    # Словарь данных, который будет отправлен в POST-запросе
    data = {
        'title': title,
        'body': body,
        'userId': user_id
    }

    # Отправляем POST-запрос с данными
    response = requests.post(url, json=data)

    # Печатаем статус-код и содержимое ответа
    print("Status Code:", response.status_code)
    print("Response Content:")
    print(response.json())


# Вызываем функцию с данными для нового поста
create_post('foo', 'bar', 1)