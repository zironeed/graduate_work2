from django.test import TestCase
from django.urls import reverse

from users.models import User
from blog.models import Post


class TestBlog(TestCase):

    def setUp(self):

        self.c_user = User(
            phone_number='2222222222',
            is_community=True,
            is_active=True,
            is_staff=False,
            is_superuser=False
        )
        self.c_user.set_password('12345')
        self.c_user.save()

        self.society_post = Post.objects.create(
            title='Society',
            description='Sooociety',
        )

        self.community_post = Post.objects.create(
            title='Community',
            description='Commmmunity',
            owner=self.c_user
        )

    def test_view_url_exists_society(self):
        resp = self.client.get('/blog/posts/society/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_exists_community(self):
        resp = self.client.get('/blog/posts/community/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_society(self):
        resp = self.client.get(reverse('blog:default_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_community(self):
        resp = self.client.get(reverse('blog:premium_list'))
        self.assertEqual(resp.status_code, 200)

    def test_list_uses_correct_template(self):
        resp = self.client.get(reverse('blog:default_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'blog/post_list.html')

    def test_detail_uses_correct_template(self):
        resp = self.client.get(reverse('blog:post_detail', kwargs={'pk': self.community_post.pk}))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'blog/post_detail.html')

    def test_create_uses_correct_template(self):
        resp = self.client.post(reverse('blog:post_create'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'blog/post_form.html')

    def test_list_post_society(self):
        resp = self.client.get(reverse('blog:default_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['post_list']) == 1)

    def test_list_post_community(self):
        resp = self.client.get(reverse('blog:premium_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['post_list']) == 1)
