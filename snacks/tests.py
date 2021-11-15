from django.urls import reverse
from django.test import TestCase
# Create your tests here.
class SnackTest(TestCase):
    def test_home_page_status_code(self):
        url = reverse("home")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):

        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")        


    def test_snack_list_status_code(self):

        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    

    def test_snack_list_template(self):
 
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")        