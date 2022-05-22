import pytest

from utils.comments import get_comment_all, get_comments_by_post_id

# Задаем, какие ключи ожидаем получать в вакансии
keys_should_be = {"post_id", "commenter_name", "comment", "pk"}


class TestComments:

    def test_get_comment_all(self, func=get_comment_all()):
        """Проверяем, верный ли список комментариев возвращается"""
        assert type(func) == list, "возвращается не список"
        assert len(func) > 0, "возвращается пустой список"
        assert set(func[0].keys()) == keys_should_be, "неверный список ключей"

    parameters_to_get_by_id = {k["post_id"] for k in get_comment_all()} # собираем в множество все id

    @pytest.mark.parametrize("comment_id", parameters_to_get_by_id)
    def test_get_comments_by_post_id(self, comment_id, func=get_comments_by_post_id):
        """Проверяем список комментариев, связанных с определенным постом"""
        for f in func(comment_id):
            assert f['post_id'] == comment_id, "комментарии не соответствуют данному посту"
        assert len(func(comment_id)) > 0, "возвращается пустой список"
        assert set(func(comment_id)[0].keys()) == keys_should_be, "неверный список ключей"

