from SeleniumInfra.infra import SeleniumInfra


class BasePage:
    def __init__(self):
        self.seleniumInfra = SeleniumInfra()

    def moveToSite(self,link):
        self.seleniumInfra.openSite("https://demo.nopcommerce.com/")
