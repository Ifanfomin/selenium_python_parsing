from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from config import vk_email, vk_password


class SeleniumVkParse(object):
    def __init__(self):
        self.driver = None
        self.create_driver()

    def create_driver(self):
        options = webdriver.FirefoxOptions()
        service = webdriver.FirefoxService(executable_path="/snap/bin/firefox.geckodriver")
        options.set_preference("profile",
                               "/home/ifan/snap/firefox/common/.mozilla/firefox/uw0658yz.profile_for_selenium")

        self.driver = webdriver.Firefox(options=options, service=service)
        self.login_vk()

    def login_vk(self):
        self.driver.get("https://vk.com/")

        self.driver.find_element("id", "index_email").send_keys(vk_email)
        self.driver.find_element("css selector", ".VkIdForm__signInButton").click()

        WebDriverWait(driver=self.driver, timeout=10).until(lambda x: x.find_element("name", "password"))

        self.driver.find_element("name", "password").send_keys(vk_password)
        self.driver.find_element("css selector", ".vkuiButton").click()
        self.search_info()

    def search_info(self):
        WebDriverWait(driver=self.driver, timeout=10).until(lambda x: x.find_element("id", "feed_rows"))
        # posts = self.driver.find_element("id", "feed_rows")
        # print(posts)
        # for post in posts:
        #     print(post)
        self.driver.quit()

if __name__ == '__main__':
    SeleniumVkParse()
