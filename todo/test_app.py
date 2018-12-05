from django.apps import apps
from django.test import TestCase
from .apps import TodoConfig

class TestTodoConfig(TestCase):
    def test_app(self):
        self.assertEquals('todo', TodoConfig.name)
        self.assertEquals('todo', apps.get_app_config('todo').name)