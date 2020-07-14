from selenium import webdriver
import unittest
import time
import selenium

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def revertChanges(self):
		#Delete the most recent work exprience
		self.browser.get('http://127.0.0.1:8000/admin/blog/workexperience/')
		time.sleep(1)
		recent_work_experience = self.browser.find_element_by_xpath("//tr[@class='row1']/th/a").get_attribute("href")
		self.browser.get(recent_work_experience)
		time.sleep(1)
		delete = self.browser.find_element_by_xpath("//p[@class='deletelink-box']/a[1]")
		self.browser.get(delete.get_attribute("href"))
		time.sleep(3)
		confirm = self.browser.find_element_by_xpath("//input[@type='submit']")
		confirm.submit()
		time.sleep(1)

		#Change education back
		self.browser.get('http://127.0.0.1:8000/admin/blog/education/2/change/')
		time.sleep(1)
		edit_qualification = self.browser.find_element_by_id("id_qualification")
		edit_qualification.clear()
		edit_qualification.send_keys("BSc Computer Science with Digital Technology Partnership with PwC")
		edit_qualification.submit()
		time.sleep(1)

		#Change skills back
		self.browser.get('http://127.0.0.1:8000/admin/blog/cv/1/change/')
		time.sleep(1)
		edit_key_skills = self.browser.find_element_by_id("id_skills")
		edit_key_skills.clear()
		edit_key_skills.send_keys("Java (intermediate),C/C++ (intermediate),Python (beginner),Haskell (beginner)")
		edit_key_skills.submit()
		time.sleep(1)

		#Delete the most recent activity
		self.browser.get('http://127.0.0.1:8000/admin/blog/activity/')
		time.sleep(1)
		recent_activity = self.browser.find_element_by_xpath("//tr[@class='row1']/th/a").get_attribute("href")
		self.browser.get(recent_activity)
		time.sleep(1)
		delete = self.browser.find_element_by_xpath("//p[@class='deletelink-box']/a[1]")
		self.browser.get(delete.get_attribute("href"))
		time.sleep(3)
		confirm = self.browser.find_element_by_xpath("//input[@type='submit']")
		confirm.submit()
		time.sleep(1)


	def login(self, username="israjc", password="superpassword"):
		username_el = self.browser.find_element_by_id("id_username")
		username_el.send_keys(username)
		password_el = self.browser.find_element_by_id("id_password")
		password_el.send_keys(password)

		password_el.submit()

	def test_can_edit_and_view_cv(self):
		
		#Isra wants to view her CV online so she visits her site
		self.browser.get('http://localhost:8000/cv/1')

		#She notices the browser title say 'CV'
		self.assertIn('CV', self.browser.title)

		#She is able to see her personal profile at the  top of the page
		time.sleep(1)
		headshot = self.browser.find_element_by_tag_name('img')
		self.assertIn("headshot.jpg", headshot.get_attribute('src'))
		name = self.browser.find_element_by_id('name_header')
		self.assertEqual(name.text, 'Isra Jawaid')
		title = self.browser.find_element_by_id('title')
		self.assertEqual(title.text, 'Degree Apprentice')

		#She logs into the admin and tries to edit her contact info 
		self.browser.get('http://127.0.0.1:8000/admin/blog/cv/1/change/')
		time.sleep(1)
		self.login()
		time.sleep(1)
		edit_website = self.browser.find_element_by_id("id_website")
		edit_website.clear()
		edit_website.send_keys("http://israjc.pythonanywhere.com")
		edit_number = self.browser.find_element_by_id("id_number")
		edit_number.clear()
		edit_number.send_keys("0123456789")

		#She also edits her personal profile
		edit_profile = self.browser.find_element_by_id("id_personal_profile")
		edit_profile.clear()
		edit_profile.send_keys("A hard-working and passionate student in second year of a BSc Computer Science degree at the University of Birmingham. I am also employed at PwC as a technology degree apprentice, having completed a summer placement at the company and looking forward to a placement year at PwC.")
		edit_profile.submit()
		time.sleep(1)

		#She goes back to her CV page to see if the information is updated
		self.browser.get('http://localhost:8000/cv/1')
		time.sleep(2)
		website = self.browser.find_element_by_id("website")
		number = self.browser.find_element_by_id("number")
		personal_profile = self.browser.find_element_by_id("personal_profile")
		self.assertEqual(website.text, 'http://israjc.pythonanywhere.com')
		self.assertIn('0123456789', number.text)
		self.assertEqual("A hard-working and passionate student in second year of a BSc Computer Science degree at the University of Birmingham. I am also employed at PwC as a technology degree apprentice, having completed a summer placement at the company and looking forward to a placement year at PwC.",
		personal_profile.text)

		#She wants to add some work experience to her CV that she recently took part in
		#She goes back to the admin page to do this and enters in details about the experience
		self.browser.get('http://127.0.0.1:8000/admin/blog/workexperience/add/')
		time.sleep(1)
		edit_title = self.browser.find_element_by_id("id_title")
		edit_company = self.browser.find_element_by_id("id_company")
		edit_duration = self.browser.find_element_by_id("id_duration")
		edit_description = self.browser.find_element_by_id("id_description")
		edit_title.send_keys("Some Work Experience")
		edit_company.send_keys("Some Company")
		edit_duration.send_keys("June 2020 to present")
		edit_description.send_keys("Description of some work experience at some company")
		edit_description.submit()
		time.sleep(1)

		#She goes back to the page to check that the new addition is shown on the page
		self.browser.get('http://localhost:8000/cv/1')
		time.sleep(3)
		work_experience_title = self.browser.find_element_by_id("work_experience_title")
		work_experience_duration = self.browser.find_element_by_id("work_experience_duration")
		work_experience_description = self.browser.find_element_by_id("work_experience_description")
		self.assertEqual("Some Work Experience at Some Company", work_experience_title.text)
		self.assertEqual("June 2020 to present", work_experience_duration.text)
		self.assertEqual("Description of some work experience at some company", work_experience_description.text)

		#She wants to change a few details about her education
		#She goes back to the admin page and decides to change the name of her degree
		self.browser.get('http://127.0.0.1:8000/admin/blog/education/2/change/')
		time.sleep(1)
		edit_qualification = self.browser.find_element_by_id("id_qualification")
		edit_qualification.clear()
		edit_qualification.send_keys("BSc Computer Science Degree")
		edit_qualification.submit()
		time.sleep(1)

		#She goes back to the page to check that the title has been updated
		self.browser.get('http://localhost:8000/cv/1')
		time.sleep(2)
		education_title = self.browser.find_element_by_id("education_title")
		self.assertIn("BSc Computer Science Degree", education_title.text)

		#She recently has been working on her python skills so wants to update this in her key skills
		#She goes to the admin page and updates her python level from beginner to intermediate
		self.browser.get('http://127.0.0.1:8000/admin/blog/cv/1/change/')
		time.sleep(1)
		edit_key_skills = self.browser.find_element_by_id("id_skills")
		edit_key_skills.clear()
		edit_key_skills.send_keys("Java (intermediate),C/C++ (intermediate),Python (intermediate),Haskell (beginner)")
		edit_key_skills.submit()
		time.sleep(1)

		#She goes back to her CV to check that this has been updated
		self.browser.get('http://localhost:8000/cv/1')
		time.sleep(2)
		key_skills = self.browser.find_elements_by_id("skills")
		self.assertIn("Python (intermediate)", [skill.text for skill in key_skills])

		#She wants to add a recent activity that she took part in so goes back to the admin page 
		self.browser.get('http://127.0.0.1:8000/admin/blog/activity/add/')
		time.sleep(1)
		edit_title = self.browser.find_element_by_id("id_title")
		edit_description = self.browser.find_element_by_id("id_description")
		edit_title.send_keys("A recent activity")
		edit_description.send_keys("A recent activity description")
		edit_description.submit()
		time.sleep(1)

		#She goes back to the cv page to check that her new activity has shown up
		self.browser.get('http://localhost:8000/cv/1')
		time.sleep(2)
		activity_title = self.browser.find_element_by_id("activity_title")
		activity_description = self.browser.find_element_by_id("activity_description")
		self.assertEqual(activity_title.text, "A recent activity")
		self.assertEqual(activity_description.text, "A recent activity description")

		self.revertChanges()

if __name__ == '__main__':
	unittest.main(warnings='ignore')