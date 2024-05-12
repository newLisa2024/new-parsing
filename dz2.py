import requests


def fetch_posts_by_user(user_id):
    # URL API, к которому мы обращаемся
    url = "https://jsonplaceholder.typicode.com/posts"

    # Параметры, которые мы передаем в запросе
    params = {
        'userId': user_id
    }

    # Отправляем GET-запрос с параметрами
    response = requests.get(url, params=params)

    # Проверяем статус ответа
    if response.status_code == 200:
        # Преобразуем ответ из формата JSON в Python объект (список словарей)
        posts = response.json()

        # Печатаем полученные записи
        for post in posts:
            print(f"Post ID: {post['id']}, Title: {post['title']}")
            print(f"Body: {post['body']}")
            print("-" * 50)  # Для визуального разделения записей
    else:
        print("Failed to fetch posts, status code:", response.status_code)


# Вызываем функцию с параметром userId равным 1
fetch_posts_by_user(1)