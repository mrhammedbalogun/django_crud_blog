from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.

class BlogTests(TestCase):
    def setup(self):
        self.user = get_user_model().objects.create_user(
        username = 'testuser',
        email = 'test@gmail.com',
        password = 'secret'
    )

    self.post = Post.objects.create(
        title = 'Super great title to test',
        body = 'Body of the test content goes here',
        author=self.user
    )

    def test_string_representation(self):
        post = Post(title = 'A simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Super great kind of testing')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Great body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_details_views(self):
        response = self.client.get('/post/i/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html') 

