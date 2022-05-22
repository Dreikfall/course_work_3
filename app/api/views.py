import logging
from flask import Blueprint, request, jsonify
from utils.posts import get_posts_all, get_post_by_pk
from utils.comments import get_comments_by_post_id

api_blueprint = Blueprint("api_blueprint", __name__)

logger = logging.getLogger("basic")


@api_blueprint.route('/api/posts')
def posts_all():
    logger.debug("Запрос всех постов через API")
    posts = get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>')
def posts_one(post_id):
    logger.debug("Запрошен пост с pk через API")
    post = get_post_by_pk(post_id)
    return jsonify(post)

