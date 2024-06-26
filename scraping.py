from selenium import webdriver
from selenium.webdriver.common.by import By


def getting_products():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)

    try:
        browser.get("https://www.mercadolivre.com.br/")

        input_search = browser.find_element(
            By.XPATH, "//input[@class='nav-search-input']"
        )
        btn_search = browser.find_element(By.XPATH, "//button[@class='nav-search-btn']")
        input_search.send_keys("monitor")
        btn_search.click()

        products_informations = browser.find_elements(
            By.XPATH,
            "//div[@class='ui-search-item__group ui-search-item__group--title'][.//h2 and .//span[@class='ui-search-reviews__rating-number']]",
        )

        products_informations_to_send_for_api = []

        for product_information in products_informations:
            datas = product_information.text
            products_informations_to_send_for_api.append({"information_product": datas})

    finally:
        browser.quit()
        return products_informations_to_send_for_api
