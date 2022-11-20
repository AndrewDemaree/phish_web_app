from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTests(SimpleTestCase):
    
    def test_url_exists_at_correct_location_homepageview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Home')

class AboutPageTests(SimpleTestCase):
    
    def test_url_exists_at_correct_location_aboutpageview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_aboutpage_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertContains(response, 'About')


class RandomPageTests(SimpleTestCase):
    
    def test_url_exists_at_correct_location_aboutpageview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_aboutpage_view(self):
        response = self.client.get(reverse('random'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'random.html')
        self.assertContains(response, 'Random')
