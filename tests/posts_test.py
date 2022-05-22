import pytest

from utils.posts import get_posts_all, get_posts_by_user, search_for_posts, get_post_by_pk

# Задаем, какие ключи ожидаем получать в вакансии
keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


class TestPosts:

    def test_get_posts_all(self, func=get_posts_all()):
        """Проверяем, верный ли список постов возвращается"""
        assert type(func) == list, "возвращается не список"
        assert len(func) > 0, "возвращается пустой список"
        assert set(func[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_posts_by_user(self, func=get_posts_by_user("leo")):
        """Проверяем принадлежат ли посты данному пользователю"""
        for f in func:
            assert f['poster_name'] == "leo", "посты не принадлежат данному пользователю"
        assert len(func) > 0, "возвращается пустой список"
        assert set(func[0].keys()) == keys_should_be, "неверный список ключей"

    def test_search_for_posts(self, func=search_for_posts("ага")):
        """Проверяем наличие ключевого слова в элементе/ах списка"""
        for f in func:
            assert "ага" in f['content'].lower(), "ключевое слово не найдено в списке"
        assert len(func) > 0, "возвращается пустой список"
        assert set(func[0].keys()) == keys_should_be, "неверный список ключей"

    parameters_to_get_by_pk = list(range(1, len(get_posts_all()) + 1))

    @pytest.mark.parametrize("post_pk", parameters_to_get_by_pk)
    def test_get_post_by_pk(self, post_pk, func=get_post_by_pk):
        """Проверяем любой пост по идентификатору"""
        assert func(post_pk)['pk'] == post_pk, "возвращается неверный пост"
        assert len(func(post_pk)) > 0, "возвращается пустой список"
        assert set(func(post_pk).keys()) == keys_should_be, "неверный список ключей"

