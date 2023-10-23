from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup as soup
from config import lms_email, lms_password


def main():
    ### create driver ###
    options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")  # hide window
    service = webdriver.FirefoxService(executable_path="/snap/bin/firefox.geckodriver")
    options.set_preference("profile",
                           "/home/ifan/snap/firefox/common/.mozilla/firefox/uw0658yz.profile_for_selenium")

    driver = webdriver.Firefox(options=options, service=service)

    ### login LMS ###
    driver.get("https://dnevnik.edumil.ru/")

    WebDriverWait(driver=driver, timeout=10).until(lambda x: x.find_element("id", "mod_dnevnik_login_base"))
    Select(driver.find_element("id", "mod_dnevnik_login_base")).select_by_value("kpku")

    driver.find_element("id", "mod_dnevnik_login_username").send_keys(lms_email)
    driver.find_element("id", "mod_dnevnik_login_password").send_keys(lms_password)
    driver.find_element("id", "mod_dnevnik_login_submit").click()

    ### get info ###
    # WebDriverWait(driver=driver, timeout=10).until(lambda x: x.find_element("id", "noNotificationsPopupClose").is_displayed())
    # driver.find_element("id", "noNotificationsPopupClose").click()  # close ADS

    driver.get("https://dnevnik.edumil.ru/component/dnevnik/?controller=dnevnik&task=dnevnik")

    page_soup = soup(driver.page_source, features="html.parser")  # start search with soup
    print(page_soup)
    # ну и т.д.

    # driver.quit()


if __name__ == '__main__':
    main()
