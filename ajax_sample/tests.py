from django.test import TestCase
from django.test.client import Client


class AjaxTestCase(TestCase):
    def setUp(self):
        pass

    def test_ajax(self):
        c = Client()
        response = c.post('/ajax_sample/input/',{'echo':'test_echo'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content,'test_echo')

