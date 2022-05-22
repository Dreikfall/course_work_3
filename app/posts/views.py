import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request, abort
from utils.posts import get_posts_all, get_post_by_pk, search_for_posts, get_posts_by_user
from utils.comments import get_comments_by_post_id

posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")

logger = logging.getLogger("basic")


@posts_blueprint.route('/')
def posts_all():
    logger.debug("Запрошены все посты")
    try:
        posts = get_posts_all()
        return render_template("index.html", posts=posts)
    except:
        return "Что-то пошло не так..."


@posts_blueprint.route('/posts/<int:post_pk>/')
def posts_one(post_pk):
    logger.debug(f'Запрошен пост {post_pk}')
    try:
        post = get_post_by_pk(post_pk)
        comments = get_comments_by_post_id(post_pk)
    except (JSONDecodeError, FileNotFoundError) as e:
        return f"Ошибка данных поста = {e}"
    except Exception as e:
        return "Неизвестная ошибка"
    else:
        if post is None:
            abort(404)
        number_of_comments = len(comments)
        return render_template("post.html", post=post, comments=comments, len=number_of_comments)


@posts_blueprint.errorhandler(404)
def post_error(e):
    return "Страница не найдена", 404


@posts_blueprint.route('/search/')
def posts_search():
    query = request.args.get("s", "")
    posts = search_for_posts(query)
    number_of_post = len(posts)
    return render_template("search.html", query=query, posts=posts, number_of_post=number_of_post)


@posts_blueprint.route('/users/<username>/')
def posts_by_user(username):
    posts = get_posts_by_user(username)
    number_of_post = len(posts)
    return render_template("user-feed.html", posts=posts, number_of_post=number_of_post)
