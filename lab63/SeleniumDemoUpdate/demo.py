from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Crawler:
	def __init__(self, base_url = 'https://www.nasdaq.com/market-activity/stocks/aapl/historical'):
		self.base_url = base_url

		### To prevent download dialog and set download location
		# set absolute path to folder to be used for downloads:
		download_folder = '/media/nemsys/data/projects/courses/netIT/PythonCourseNetIT/PythonCourse_25.10-Labs/lab63/SeleniumDemoUpdate/data/'

		chrome_options = Options()
		prefs = {
			'download.prompt_for_download' : False,
			'download.default_directory':download_folder
		}
		chrome_options.add_experimental_option("prefs", prefs)

		### start in maximized window
		chrome_options.add_argument('start-maximized')


		### init driver dynamically (without specifying installation path):
		# Reference: https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
		service = Service(executable_path=ChromeDriverManager().install())
		self.driver = webdriver.Chrome(service=service,options=chrome_options)

		### send get request:
		self.driver.get(self.base_url);

		### click on Accept Cookies button, after it is shown:
		WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#onetrust-accept-btn-handler'))).click()


	def get_table_rows(self):
		# Get TR elements only when they are loaded - best practice:
		table_rows = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'tr.historical-data__row')))

		# next will work if elements are loaded, but we can not be sure when they will
		# table_rows = self.driver.find_elements(By.CSS_SELECTOR, 'tr.historical-data__row')

		print(f'Scraped {len(table_rows)} data rows.')
		for row in table_rows:
			print(row.text)

	def download_data(self):
		# click on "Download data" button only when it is ready:
		WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
			(By.CSS_SELECTOR,'.historical-data__controls-button--download'))
		).click()


	def start(self):
		print('Test getting table rows:')
		self.get_table_rows()

		print('Test download data: ')
		self.download_data()
		print('File is downloaded!')

if __name__ == '__main__':
	crawler = Crawler()
	crawler.start()
