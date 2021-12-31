from selenium import webdriver
from pages.BasePage import BasePage


class SeleniumInfraDriver:
    def __init__(self):
        self.seleniumInfra = BasePage()
