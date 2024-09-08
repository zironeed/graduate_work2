from django.test import TestCase
from django.urls import reverse


class TestBlog(TestCase):

    def test_view_url_exists_login(self):
        resp = self.client.get('/users/login/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_exists_registration(self):
        resp = self.client.get('/users/user/registration/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_login(self):

        resp = self.client.get(reverse('users:login'))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_registration(self):

        resp = self.client.get(reverse('users:user_register'))
        self.assertEqual(resp.status_code, 200)

    def test_login_uses_correct_template(self):

        resp = self.client.get(reverse('users:login'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'users/login.html')

    def test_registration_uses_correct_template(self):

        resp = self.client.get(reverse('users:user_register'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'users/register.html')
