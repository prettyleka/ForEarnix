from selenium.webdriver.common.by import By


class ProductPageLocators:
    def __init__(self):
        self.moveToDetails = (By.XPATH, "//div[@class='item-box']//a[contains(@title,'details')]")
        self.shortDescription = (By.XPATH, "//div[@class='short-description']")
        self.fullDescription = (By.XPATH, "//div[@class='full-description']")
        self.price = (By.XPATH, "//div[@class='product-price']/span")
        self.product = (By.XPATH, "//div[@class='item-box']/div[@class='product-item']")
        self.prices = (By.XPATH, '//div[@class="prices"]/span')