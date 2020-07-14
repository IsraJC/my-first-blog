from django.test import TestCase
from django.contrib import auth

class CVPageTest(TestCase):

	def test_uses_cv_template(self):
		response = self.client.get('/cv/1/')
		self.assertTemplateUsed(response, 'blog/cv_page.html')


	def test_uses_edit_cv_template(self):
		response = self.client.get('/cv/1/edit/')
		self.assertTemplateUsed(response, 'blog/edit_cv_page.html')


