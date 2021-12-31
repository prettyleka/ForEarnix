from selenium.webdriver.common.by import By


class LandingPageLocators:
    def __init__(self):
        self.searchInput = (By.XPATH, "//input[@class='search-box-text ui-autocomplete-input']")
        self.btnSearch = (By.XPATH, "//button[@class='button-1 search-box-button']")
        self.notMobileUpperPanel = lambda tab:(By.XPATH, f"//ul[@class='top-menu notmobile']//a[@href='/{tab}']")
        self.notMobileComputerMenu = lambda name:(By.XPATH, f"//ul[@class='top-menu notmobile']//a[@href='/computers']/parent::li//a[@href='/{name}']")
