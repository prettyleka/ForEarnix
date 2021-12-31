from ForEarnix.SeleniumInfra.infra import SeleniumInfra
from ForEarnix.pages.BasePage import BasePage
from ForEarnix.pages.LandingPage.LandingaPage import LandingPage
from ForEarnix.pages.ProductPage.ProductPage import ProductPage

class InitPagesWithDriver:
    def __init__(self):
        self.seleniumInfra = SeleniumInfra()
        self.bp = BasePage(self.seleniumInfra)
        self.lp = LandingPage(self.seleniumInfra)
        self.pg = ProductPage(self.seleniumInfra)