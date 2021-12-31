from ForEarnix.SeleniumInfra.infra import SeleniumInfra
from ForEarnix.pages.LandingPage.LandingPageLocators import LandingPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class LandingPage:
    def __init__(self, seleniumInfra:SeleniumInfra):
        self.seleniumInfra = seleniumInfra
        self.locators = LandingPageLocators()

    def writeInSearchField(self, word):
        inputField = self.seleniumInfra.findElementBy(*self.locators.searchInput)
        self.seleniumInfra.write(data=word,element=inputField)

    def clickOnSearchBtn(self):
        self.seleniumInfra.clickButton(*self.locators.btnSearch)

    def hoverOnNotMobileTab(self, tab):
        self.seleniumInfra.hoverWithMouse(*self.locators.notMobileUpperPanel(tab))

    def clickOnNitMobileComputerMenuBtns(self, name):
        self.seleniumInfra.clickButton(*self.locators.notMobileComputerMenu(name))
