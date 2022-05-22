import json


def get_comment_all():
    """Возвращает список всех комментариев"""

    with open("data/comments.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_comments_by_post_id(post_id):
    """Возвращает список комментариев определенного поста"""

    list_comment = []
    comments = get_comment_all()
    for comment in comments:
        if comment['post_id'] == post_id:
            list_comment.append(comment)
    return list_comment
