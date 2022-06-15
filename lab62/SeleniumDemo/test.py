import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def get_title_nodes(driver):
	titles = driver.find_elements(by=By.CSS_SELECTOR, value="div.card-title")

	for title_node in titles:
		title = title_node.find_element(by=By.CSS_SELECTOR, value="span:nth-of-type(2)")
		print(title.text)

	# print(titles)
	return titles

driver = webdriver.Chrome('/media/nemsys/data/projects/courses/netIT/PythonCourseNetIT/PythonCourse_25.10-Labs/lab62/chromedriver')  # Optional argument, if not specified will search path.

driver.get('https://www.jobs.bg/front_job_search.php?subm=1&keywords%5B%5D=python');

time.sleep(2) # Let the user actually see something!

btnCookies = driver.find_element_by_css_selector('button[onclick="closeCookieBar();"]')
btnCookies.click()



titles = get_title_nodes(driver)


time.sleep(2)
 # Scroll down to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# search_box = driver.find_element_by_name('q')

# search_box.send_keys('ChromeDriver')

# search_box.submit()

# time.sleep(5) # Let the user actually see something!

# driver.quit()