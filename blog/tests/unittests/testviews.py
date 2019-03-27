from blog import views
from blog.models import Post
from django.urls import reverse, resolve
from django.test import TestCase


class ViewTests(TestCase):


    def test_blog_exists(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_url_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEquals(response.status_code, 200)

    def test_template_post_list_used(self):
        response = self.client.get(reverse('post_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'blog/post_list.html')
        self.assertTemplateUsed(response,'blog/base.html')

    def test_post_list_contains_expected_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>list</title>')

    def test_post_list_contains_expected_html2(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1><a href="/">Django Girls Blog</a></h1>')

    def test_post_list_does_not_contain_unexpected_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'this sentence should not be on the page')

    def test_drafts_page_exists(self):
        response = self.client.get('/drafts/')
        self.assertEquals(response.status_code, 200)

    def test_drafts_page_url(self):
        response = self.client.get(reverse('post_draft_list'))
        self.assertEquals(response.status_code, 200)

    def test_template_post_draft_list_used(self):
        response = self.client.get(reverse('post_draft_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'blog/post_draft_list.html')
        self.assertTemplateUsed(response,'blog/base.html')

    def test_post_list_contains_expected_html(self):
        response = self.client.get('/drafts/')
        self.assertContains(response, '<title>Django Girls blog</title>')

    def test_post_list_does_not_contain_unexpected_html(self):
        response = self.client.get('/drafts/')
        self.assertNotContains(response, 'this sentence should not be on the page')
