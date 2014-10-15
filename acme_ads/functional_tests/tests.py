from django.test import LiveServerTestCase
from selenium import webdriver


class AdManagementTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_create_and_view_ad(self):
		#Carl wants to create a new ad on his new fangled web app. so he goes to the homepage
		self.browser.get(self.live_server_url)

		#Carl then clicks on the nav link 'Create Ad' and is redirected to '/ads/create'
		create_ad_link = self.browser.find_element_by_class_name('nav--create-ad')
		create_ad_link.click()

		#Carl types in the name of the new ad and the ad contents and clicks submit
		#Carl is redirected to the ad details page located at '/ads/:id' and sees his newly created ad