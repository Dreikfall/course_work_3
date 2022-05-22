import pytest

from run import app


class TestAPI:

    def test_app_all_posts_status_code(self):
        """ Проверяем, получается ли нужный статус-код """
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, "Статус код всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_app_one_posts_status_code(self):
        response = app.test_client().get('/api/posts/1', follow_redirects=True)
        assert response.status_code == 200, "Статус код всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

