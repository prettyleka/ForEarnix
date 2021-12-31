from ForEarnix.SeleniumInfra.infra import SeleniumInfra
from ForEarnix.pages.ProductPage.ProductPageLocators import ProductPageLocators


class ProductPage:
    def __init__(self, seleniumInfra:SeleniumInfra):
        self.seleniumInfra = seleniumInfra
        self.locators = ProductPageLocators()

    def moveToProductDescription(self):
        self.seleniumInfra.clickButton(*self.locators.moveToDetails)

    def getShortDescription(self):
        short = self.seleniumInfra.findElementBy(*self.locators.shortDescription)
        text=self.seleniumInfra.getTextFromElement(element=short)
        print("short text is: "+text)
        return text

    def getFullDescription(self):
        full = self.seleniumInfra.findElementBy(*self.locators.fullDescription)
        text=self.seleniumInfra.getTextFromElement(element=full)
        print("full text is: "+text)
        return text

    def getPrice(self):
        price = self.seleniumInfra.findElementBy(*self.locators.price)
        text=self.seleniumInfra.getTextFromElement(element=price)
        print("price is: "+text)
        return text

    def sumOfAllPrices(self):
        priceEl=self.seleniumInfra.findElementListBy(*self.locators.prices)
        summ=0
        for x in priceEl:
            price= self.seleniumInfra.getTextFromElement(element=x)
            priceOnlyNum=price.split("$")[1].replace(".00", "").replace(",", "")
            summ=summ+int(priceOnlyNum)
        print(summ)
        return summ

    def sumOfHiddenIds(self):
        elements=self.seleniumInfra.findElementListBy(*self.locators.product)
        summ = 0
        for x in elements:
            hiddenID = int(x.get_attribute("data-productid"))
            summ = summ + hiddenID
        print(summ)
        return summ

