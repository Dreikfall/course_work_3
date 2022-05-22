import json


def get_posts_all():
    """Возвращает список всех постов"""

    with open("data/data.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_posts_by_user(user_name):
    """Возвращает список постов определенного пользователя"""

    list_posts = []
    posts = get_posts_all()
    for post in posts:
        if post['poster_name'].lower() == user_name.lower():
            list_posts.append(post)
    return list_posts


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""

    list_posts = []
    str_punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    posts = get_posts_all()
    for post in posts:
        edited_line = post['content'].lower()  # присваиваем текст контента к переменной
        for mark in str_punctuation:  # очищаем его от пунктуации
            if mark in edited_line:
                edited_line = edited_line.replace(mark, "")
        if query is not None and query.lower() in edited_line.strip().split():  # добавляем в список по ключевому слову
            list_posts.append(post)
    return list_posts


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""

    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post
