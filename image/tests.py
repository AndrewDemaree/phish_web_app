from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from .models import Comment
# Create your tests here.
class ImageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret", favorite_fish = "Clownfish", favorite_phish_song = "Reba", age = 7
        )
        cls.comment = Comment.objects.create(
            author=cls.user, comment="Tweedledee"
        )

    def test_post_model(self):
        self.assertEqual(self.comment.author.username, "testuser")
        self.assertEqual(self.comment.comment, "Tweedledee")
        self.assertEqual(self.comment.get_absolute_url(), "/chat/1/")
    def test_url_exists_at_correct_location(self):
        response_list = self.client.get("/chat/")
        response_new = self.client.get("/chat/new/")
        response_detail = self.client.get("/chat/1/")
        self.assertEqual(response_list.status_code, 200)
        self.assertEqual(response_new.status_code, 200)
        self.assertEqual(response_detail.status_code, 200)
    def test_comment_views(self):
        response_list = self.client.get(reverse("comment"))
        response_detail = self.client.get(reverse("comment_detail", kwargs={'pk': self.comment.pk}))
        no_response_detail = self.client.get("/comment/100000/")
        self.assertEqual(response_list.status_code, 200)
        self.assertTemplateUsed(response_list, "Comment.html")
        self.assertEqual(response_detail.status_code, 200)
        self.assertEqual(no_response_detail.status_code, 404)
        self.assertTemplateUsed(response_detail, "Chat_detail.html")
