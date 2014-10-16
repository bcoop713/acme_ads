from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ads.models import Ad
from newspapers.models import Newspaper


class AdCreationTest(StaticLiveServerTestCase):

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


class AdNavigationTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

		ad1 = Ad()
		ad1.name = 'Test Ad 1'
		ad1.content = 'Content 1'
		ad1.save()

		ad2 = Ad()
		ad2.name = 'Test Ad 2'
		ad2.content = 'Content 2'
		ad2.save()

		ad3 = Ad()
		ad3.name = 'Test Ad 3'
		ad3.content = 'Content 3'
		ad3.save()

	def tearDown(self):
		self.browser.quit()

	def test_can_view_ad_list(self):
		#Edith wants to check out a list of all her ads so she starts off at the home page
		self.browser.get(self.live_server_url)


		#Edith then clicks on the "My Ads" link and is directed to /ads/
		my_ads_link = self.browser.find_element_by_class_name('nav--my-ads')
		my_ads_link.click()
		self.assertEqual(self.browser.current_url, self.live_server_url + '/ads/')


		#Edith peruses the list of links and clicks on one to view its details
		ad_list = self.browser.find_elements_by_class_name('ad-list--name')
		self.assertEqual(len(ad_list), 3)

		#Edith is redirected to its detail page and happily views the Ad details
		link = ad_list[1].find_element_by_tag_name('a')
		link.click()
		self.assertRegex(self.browser.current_url, '/ads/\d+/')

		content = self.browser.find_element_by_class_name('ad-detail--content').text
		self.assertEqual(content, 'Content 2')


class NewspaperCreationTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_create_and_view_a_newspaper(self):
		#Jasper wants to create a new ad so he goes to the web root
		self.browser.get(self.live_server_url)


		#Jasper clicks on the nav link "Create Newspaper" and is redirected to /newspapers/create/
		create_newspaper_link = self.browser.find_element_by_class_name('nav--create-newspaper')
		create_newspaper_link.click()
		self.assertEqual(self.browser.current_url, self.live_server_url + '/newspapers/create/')

		
		#Jasper types in the name of the new newspaper and clicks submit
		newspaper_name_input = self.browser.find_element_by_class_name('create-newspaper--name--input')
		newspaper_name_input.send_keys('Test Newspaper 1')
		self.browser.find_element_by_class_name('create-newspaper--submit').click()

		
		#Jasper gets redirected to the newspaper detail page at /newspapers/:id/
		self.assertRegex(self.browser.current_url, '/newspapers/\d+/')


		#Jasper sees his newly created newspaper and is in awe
		newspaper_name = self.browser.find_element_by_class_name('newspaper-detail--name').text
		self.assertEqual(newspaper_name, 'Test Newspaper 1')


class NewspaperNavigationTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

		newspaper1 = Newspaper()
		newspaper1.name = 'Test Newspaper 1'
		newspaper1.save()

		newspaper2 = Newspaper()
		newspaper2.name = 'Test Newspaper 2'
		newspaper2.save()

		newspaper3 = Newspaper()
		newspaper3.name = 'Test Newspaper 3'
		newspaper3.save()

	def tearDown(self):
		self.browser.quit()

	def test_can_view_newspaper_list(self):
		#Peggy wants to check out a list of all her newspapers so she starts off at the home page
		self.browser.get(self.live_server_url)


		#Peggy then clicks on the "My Newspapers" link and is directed to /newspapers/
		my_newspapers_link = self.browser.find_element_by_class_name('nav--my-newspapers')
		my_newspapers_link.click()
		self.assertEqual(self.browser.current_url, self.live_server_url + '/newspapers/')


		#Peggy peruses the list of links and clicks on one to view its details
		newspaper_list = self.browser.find_elements_by_class_name('newspaper-list--name')
		self.assertEqual(len(newspaper_list), 3)

		#Peggy is redirected to its detail page and happily views the Newspaper details
		link = newspaper_list[1].find_element_by_tag_name('a')
		link.click()
		self.assertRegex(self.browser.current_url, '/newspapers/\d+/')

		name = self.browser.find_element_by_class_name('newspaper-detail--name').text
		self.assertEqual(name, 'Test Newspaper 2')


class AdAndNewspaperRelationTest(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

		newspaper1 = Newspaper()
		newspaper1.name = 'Test Newspaper 1'
		newspaper1.save()

		newspaper2 = Newspaper()
		newspaper2.name = 'Test Newspaper 2'
		newspaper2.save()

		newspaper3 = Newspaper()
		newspaper3.name = 'Test Newspaper 3'
		newspaper3.save()

		ad1 = Ad()
		ad1.name = 'Test Ad 1'
		ad1.content = 'Content 1'
		ad1.save()

		ad2 = Ad()
		ad2.name = 'Test Ad 2'
		ad2.content = 'Content 2'
		ad2.save()
		ad2.newspapers.add(newspaper1, newspaper2)
		ad2.save()

		ad3 = Ad()
		ad3.name = 'Test Ad 3'
		ad3.content = 'Content 3'
		ad3.save()

	def tearDown(self):
		self.browser.quit()

	def test_view_newspaper_to_ad_relations(self):
		#Ernest wants to see what newspapers an ad is in
		#So he goes to /ads/2/
		self.browser.get(self.live_server_url + '/ads/2/')


		#Ernest sees a list of newspapers that the ad is currently running in
		free_newspaper_list = self.browser.find_elements_by_class_name('ad-detail--free-newspaper')


		#Ernest also notices a list of newspapers that the ad is NOT currently running in
		connected_newspaper_list = self.browser.find_elements_by_class_name('ad-detail--connected-newspaper')
