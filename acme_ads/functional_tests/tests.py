from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AdManagementTest(StaticLiveServerTestCase):

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
		self.assertEqual(self.browser.current_url, self.live_server_url + '/ads/create/')


		#Carl types in the name of the new ad and the ad contents and clicks submit
		ad_name_input = self.browser.find_element_by_class_name('create-ad--name--input')
		ad_content_input = self.browser.find_element_by_class_name('create-ad--content--input')
		ad_name_input.send_keys('Test Ad 1')
		ad_content_input.send_keys('Buy our stuff now')
		self.browser.find_element_by_class_name('create-ad--submit').click()


		#Carl is redirected to the ad details page located at '/ads/:id' and sees his newly created ad
		self.assertRegex(self.browser.current_url, '/ads/\d+/')
		ad_name = self.browser.find_element_by_class_name('ad-detail--name')
		ad_content = self.browser.find_element_by_class_name('ad-detail--content')

		self.assertEqual(ad_name.text, 'Test Ad 1')
		self.assertEqual(ad_content.text, 'Buy our stuff now')
